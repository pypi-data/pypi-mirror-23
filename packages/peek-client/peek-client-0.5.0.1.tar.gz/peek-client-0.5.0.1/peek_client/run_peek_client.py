#!/usr/bin/env python
"""
 * synnova.py
 *
 *  Copyright Synerty Pty Ltd 2013
 *
 *  This software is proprietary, you are not free to copy
 *  or redistribute this code in any format.
 *
 *  All rights to this software are reserved by
 *  Synerty Pty Ltd
 *
"""
from pytmpdir.Directory import DirSettings
from twisted.internet.defer import inlineCallbacks
from txhttputil.site.FileUploadRequest import FileUploadRequest
from txhttputil.site.SiteUtil import setupSite
from txhttputil.util.DeferUtil import printFailure
from txhttputil.util.LoggingUtil import setupLogging
from vortex.DeferUtil import vortexLogFailure

from peek_plugin_base.PeekVortexUtil import peekClientName, peekServerName
from vortex.VortexFactory import VortexFactory

setupLogging()

from twisted.internet import reactor

import logging

# EXAMPLE LOGGING CONFIG
# Hide messages from vortex
# logging.getLogger('txhttputil.vortex.VortexClient').setLevel(logging.INFO)

# logging.getLogger('peek_client_pof.realtime.RealtimePollerEcomProtocol'
#                   ).setLevel(logging.INFO)

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# Set the parallelism of the database and reactor
reactor.suggestThreadPoolSize(10)


def setupPlatform():
    from peek_platform import PeekPlatformConfig
    PeekPlatformConfig.componentName = peekClientName

    # Tell the platform classes about our instance of the PluginSwInstallManager
    from peek_client.sw_install.PluginSwInstallManager import PluginSwInstallManager
    PeekPlatformConfig.pluginSwInstallManager = PluginSwInstallManager()

    # Tell the platform classes about our instance of the PeekSwInstallManager
    from peek_client.sw_install.PeekSwInstallManager import PeekSwInstallManager
    PeekPlatformConfig.peekSwInstallManager = PeekSwInstallManager()

    # Tell the platform classes about our instance of the PeekLoaderBase
    from peek_client.plugin.ClientPluginLoader import ClientPluginLoader
    PeekPlatformConfig.pluginLoader = ClientPluginLoader()

    # The config depends on the componentName, order is important
    from peek_client.PeekClientConfig import PeekClientConfig
    PeekPlatformConfig.config = PeekClientConfig()

    # Set default logging level
    logging.root.setLevel(PeekPlatformConfig.config.loggingLevel)

    # Initialise the txhttputil Directory object
    DirSettings.defaultDirChmod = PeekPlatformConfig.config.DEFAULT_DIR_CHMOD
    DirSettings.tmpDirPath = PeekPlatformConfig.config.tmpPath
    FileUploadRequest.tmpFilePath = PeekPlatformConfig.config.tmpPath


def main():
    # defer.setDebugging(True)
    # sys.argv.remove(DEBUG_ARG)
    # import pydevd
    # pydevd.settrace(suspend=False)

    setupPlatform()

    # Import remaining components
    from peek_client import importPackages
    importPackages()

    # Make the agent restart when the server restarts, or when it looses connection
    def restart(status):
        from peek_platform import PeekPlatformConfig
        PeekPlatformConfig.peekSwInstallManager.restartProcess()

    (VortexFactory.subscribeToVortexStatusChange(peekServerName)
        .filter(lambda online:online == False)
        .subscribe(on_next=restart)
     )

    # First, setup the VortexServer Agent
    from peek_platform import PeekPlatformConfig
    d = VortexFactory.createTcpClient(PeekPlatformConfig.componentName,
                                       PeekPlatformConfig.config.peekServerHost,
                                       PeekPlatformConfig.config.peekServerVortexTcpPort)

    # Start Update Handler,
    # Add both, The peek client might fail to connect, and if it does, the payload
    # sent from the peekSwUpdater will be queued and sent when it does connect.
    from peek_platform.sw_version.PeekSwVersionPollHandler import peekSwVersionPollHandler

    d.addErrback(vortexLogFailure, logger, consumeError=True)
    d.addCallback(lambda _: peekSwVersionPollHandler.start())

    # Start client main data observer, this is not used by the plugins
    # (Initialised now, not as a callback)
    from peek_client.backend import ClientObservable

    # Load all Plugins
    d.addErrback(vortexLogFailure, logger, consumeError=True)
    d.addCallback(lambda _: PeekPlatformConfig.pluginLoader.loadAllPlugins())

    def startSite(_):
        from peek_client.backend.SiteRootResource import setupMobile, mobileRoot
        from peek_client.backend.SiteRootResource import setupDesktop, desktopRoot

        setupMobile()
        setupDesktop()

        # Create the vortex server
        VortexFactory.createServer(PeekPlatformConfig.componentName, mobileRoot)

        mobileSitePort = PeekPlatformConfig.config.mobileSitePort
        setupSite("Peek Mobile Site", mobileRoot, mobileSitePort, enableLogin=False)

        webSocketPort = PeekPlatformConfig.config.webSocketPort
        VortexFactory.createWebsocketServer(
            PeekPlatformConfig.componentName, webSocketPort)

        desktopSitePort = PeekPlatformConfig.config.desktopSitePort
        setupSite("Peek Desktop Site", desktopRoot, desktopSitePort, enableLogin=False)

    d.addCallback(startSite)

    def startedSuccessfully(_):
        logger.info('Peek Client is running, version=%s',
                    PeekPlatformConfig.config.platformVersion)
        return _

    d.addErrback(vortexLogFailure, logger, consumeError=True)
    d.addCallback(startedSuccessfully)

    reactor.addSystemEventTrigger('before', 'shutdown', VortexFactory.shutdown)
    reactor.addSystemEventTrigger('before', 'shutdown',
                                  PeekPlatformConfig.pluginLoader.unloadAllPlugins)

    reactor.run()


if __name__ == '__main__':
    main()
