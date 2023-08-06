import asyncio
from asyncio import AbstractEventLoop

import sc2replaysearch

from .gameclient import GameClient
from .jsonparsinghttpclient import get_json_response
from .replayhandler import ReplayHandler, NoOpReplayHandler
from .replaynotifier import ReplayNotifier

GAME_STATE_ENDPOINT = "http://localhost:6119/game"
UI_STATE_ENDPOINT = "http://localhost:6119/ui"


def create_replay_notifier(
        replay_handler: ReplayHandler = NoOpReplayHandler(),
        event_loop: AbstractEventLoop = asyncio.get_event_loop()) -> ReplayNotifier:

    """
    Create a replay notifier that watches for new replays and handles them using the provided ReplayHandler

    :param replay_handler:
    :param event_loop:
    :return: a ReplayNotifier
    """

    async def get_game_object() -> dict:
        return await get_json_response(GAME_STATE_ENDPOINT)

    async def get_ui_object() -> dict:
        return await get_json_response(UI_STATE_ENDPOINT)

    return ReplayNotifier(
        GameClient(get_game_object, get_ui_object),
        sc2replaysearch.find_most_recent_replay,
        replay_handler,
        event_loop)
