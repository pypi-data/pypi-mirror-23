#!/usr/bin/env python
# -*- coding: utf-8 -*-

from channels.routing import route

from otree.channels import consumers
from otree.extensions import get_extensions_modules


channel_routing = [
    route(
        'websocket.connect', consumers.connect_wait_page,
        path=r'^/wait_page/(?P<params>[\w,]+)/$'),
    route(
        'websocket.disconnect', consumers.disconnect_wait_page,
        path=r'^/wait_page/(?P<params>[\w,]+)/$'),
    route(
        'websocket.connect', consumers.connect_group_by_arrival_time,
        path=r'^/group_by_arrival_time/(?P<params>[\w,\.]+)/$'),
    route(
        'websocket.disconnect', consumers.disconnect_group_by_arrival_time,
        path=r'^/group_by_arrival_time/(?P<params>[\w,\.]+)/$'),
    route(
        'websocket.connect', consumers.connect_auto_advance,
        path=r'^/auto_advance/(?P<params>[\w,]+)/$'),
    route('websocket.disconnect', consumers.disconnect_auto_advance,
          path=r'^/auto_advance/(?P<params>[\w,]+)/$'),
    route('websocket.connect', consumers.connect_wait_for_session,
          path=r'^/wait_for_session/(?P<pre_create_id>\w+)/$'),
    route('websocket.disconnect', consumers.disconnect_wait_for_session,
          path=r'^/wait_for_session/(?P<pre_create_id>\w+)/$'),
    route('otree.create_session',
          consumers.create_session),
    route('websocket.connect',
          consumers.connect_room_participant,
          path=r'^/wait_for_session_in_room/(?P<params>[\w,]+)/$'),
    route('websocket.disconnect',
          consumers.disconnect_room_participant,
          path=r'^/wait_for_session_in_room/(?P<params>[\w,]+)/$'),
    route('websocket.connect',
          consumers.connect_room_admin,
          path=r'^/room_without_session/(?P<room>\w+)/$'),
    route('websocket.disconnect',
          consumers.disconnect_room_admin,
          path=r'^/room_without_session/(?P<room>\w+)/$'),
    route('websocket.connect',
          consumers.connect_browser_bots_client,
          path=r'^/browser_bots_client/(?P<session_code>\w+)/$'),
    route('websocket.disconnect',
          consumers.disconnect_browser_bots_client,
          path=r'^/browser_bots_client/(?P<session_code>\w+)/$'),
    route('websocket.connect',
          consumers.connect_browser_bot,
          path=r'^/browser_bot_wait/$'),
    route('websocket.disconnect',
          consumers.disconnect_browser_bot,
          path=r'^/browser_bot_wait/$'),

]

for extensions_module in get_extensions_modules('routing'):
    channel_routing += getattr(extensions_module, 'channel_routing', [])
