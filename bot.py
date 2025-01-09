# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext, MessageFactory
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        # Extract the user's message
        message = str(turn_context.activity.text).lower()
        
        # Determine the response
        if message == "hi":
            response = "hello"
        elif message == "weather":
            response = "it's sunny"
        else:
            response = "i don't understand"
        
        # Send the response
        return await turn_context.send_activity(MessageFactory.text(response))
    
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
