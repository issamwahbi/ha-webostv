"""Constants used for LG webOS Smart TV Issam."""
import asyncio

from aiowebostv import WebOsTvCommandError
from homeassistant.const import Platform
from websockets.exceptions import ConnectionClosed, ConnectionClosedOK

DOMAIN = "webostv2"
PLATFORMS = [Platform.MEDIA_PLAYER]
DATA_CONFIG_ENTRY = "config_entry"
DATA_HASS_CONFIG = "hass_config"
DEFAULT_NAME = "LG webOS Smart TV Issam "

ATTR_BUTTON = "button"
ATTR_CONFIG_ENTRY_ID = "entry_id"
ATTR_PAYLOAD = "payload"
ATTR_SOUND_OUTPUT = "sound_output"

CONF_ON_ACTION = "turn_on_action"
CONF_SOURCES = "sources"

SERVICE_BUTTON = "button"
SERVICE_COMMAND = "command"
SERVICE_SELECT_SOUND_OUTPUT = "select_sound_output"

LIVE_TV_APP_ID = "com.webos.app.livetv"

WEBOSTV_EXCEPTIONS = (
    OSError,
    ConnectionClosed,
    ConnectionClosedOK,
    ConnectionRefusedError,
    WebOsTvCommandError,
    asyncio.TimeoutError,
    asyncio.CancelledError,
)
