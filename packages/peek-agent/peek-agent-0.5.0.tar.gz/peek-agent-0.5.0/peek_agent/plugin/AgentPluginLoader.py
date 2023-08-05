import logging
from typing import Type, Tuple

from peek_agent.plugin.PeekAgentPlatformHook import PeekAgentPlatformHook
from peek_platform.plugin.PluginLoaderABC import PluginLoaderABC
from peek_plugin_base.PluginCommonEntryHookABC import PluginCommonEntryHookABC
from peek_plugin_base.agent.PluginAgentEntryHookABC import PluginAgentEntryHookABC

logger = logging.getLogger(__name__)


class AgentPluginLoader(PluginLoaderABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        assert cls._instance is None, "AgentPluginLoader is a singleton, don't construct it"
        cls._instance = PluginLoaderABC.__new__(cls)
        return cls._instance

    @property
    def _entryHookFuncName(self) -> str:
        return "peekAgentEntryHook"

    @property
    def _entryHookClassType(self):
        return PluginAgentEntryHookABC

    @property
    def _platformServiceNames(self) -> [str]:
        return ["agent"]

    def _loadPluginThrows(self, pluginName: str,
                          EntryHookClass: Type[PluginCommonEntryHookABC],
                          pluginRootDir: str,
                          requiresService: Tuple[str, ...]) -> None:
        # Everyone gets their own instance of the plugin API
        platformApi = PeekAgentPlatformHook()

        pluginMain = EntryHookClass(pluginName=pluginName,
                                    pluginRootDir=pluginRootDir,
                                    platform=platformApi)

        # Load the plugin
        pluginMain.load()

        # Start the Plugin
        pluginMain.start()

        self._loadedPlugins[pluginName] = pluginMain
