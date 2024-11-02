import os
from autogen import ConversableAgent, GroupChat, GroupChatManager

# Phase 1
from Kouhei import return_prompt as Kouhei_prompt
from masami import return_prompt as masami_prompt
from susumu import return_prompt as susumu_prompt
from prompt import *
import autogen

from queue import Queue

message_queue = Queue()
api_key = os.getenv('api_key')

config = {
    "config_list": [{"model": "gpt-4o", "api_key": api_key}],
    "cache_seed": None,
    # "callback": None
}


def print_messages(recipient, messages, sender, config):
    message_dict = {
        "agent_name": messages[-1]["name"],
        "content": messages[-1]["content"]
    }
    message_queue.put(message_dict)
    print("yes")
    return False, None  # Returning False to indicate no further action


def create_agent(name, prompt):
    """Create a ConversableAgent with a silent configuration."""
    return ConversableAgent(
        name=name,
        system_message=prompt,
        llm_config=config,  # Making agent silent
        silent=True,
    )


def initiate_phase(phase_num, initial_message):
    """Initiate a phase with agents and manage group chat."""
    # Define prompts for each agent
    Kouhei_phase = Kouhei_prompt(f"phase_{phase_num}_prompt")
    masami_phase = masami_prompt(f"phase_{phase_num}_prompt")
    susumu_phase = susumu_prompt(f"phase_{phase_num}_prompt")

    # Create agents
    moderator = create_agent("Detective", f"moderator_{phase_num}")
    Kouhei = create_agent("Kouhei", Kouhei_phase)
    masami = create_agent("masami", masami_phase)
    susumu = create_agent("susumu", susumu_phase)

    Kouhei.register_reply(
        [autogen.Agent, None],
        reply_func=print_messages,
        config={"callback": None},
    )
    masami.register_reply(
        [autogen.Agent, None],
        reply_func=print_messages,
        config={"callback": None},
    )
    susumu.register_reply(
        [autogen.Agent, None],
        reply_func=print_messages,
        config={"callback": None},
    )

        # Initialize group chat
    group_chat = GroupChat(
        agents=[Kouhei, masami, susumu],
        messages=[] if phase_num == 1 else phase_messages,
        # max_round=4 if phase_num == 1 else None,  # Only set max_round if phase_num is 1
        speaker_selection_method="round_robin" if phase_num == 1 else "auto",
    )

        # Group Chat Manager
    group_chat_manager = GroupChatManager(
        groupchat=group_chat,
        llm_config=config,
        system_message=f"moderator_{phase_num}",
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"].lower(),
    )

    # Initiate chat
    moderator.initiate_chat(group_chat_manager, message=initial_message)

    return group_chat.messages



# Execute phases
phase_messages = []

def runcov():
    for i in range(1, 6):  # Loop through phases 1 to 5
        initial_message = f"begin phase {i}" if i > 1 else "start phase 1"
        phase_messages = initiate_phase(i, initial_message)

# Final messages from all phases are stored in 'phase_messages'
