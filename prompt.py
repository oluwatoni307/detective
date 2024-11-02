phase_summary = """
Introduction: Each player introduces themselves—name, profession, and a connection to the victim. Remember, everyone is a suspect. Introduce yourself in a way that barely scratches the surface but hints at possible motives or strained relationships. Avoid friendly tones; any one of these people might know something incriminating.

Evidence Analysis: As you examine the crime scene together, doubt each other's intentions. Any observation you make might turn into an accusation later. If someone seems overly familiar with the details, don’t hesitate to voice your suspicion. Let your responses be sharp, leaving subtle barbs or hints of distrust.

Questioning: Now, press each other for answers. Raise pointed questions about behaviors, alibis, or connections to the victim. Don’t hold back. Respond in ways that deflect suspicion, and throw questions back at anyone who digs too deeply. Trust no answer, and make others feel the heat of your suspicions.

Theory Development: Now’s your chance to build a theory around someone else’s guilt. Don’t mince words; challenge each other’s conclusions sharply, especially if you’re being accused. Deflect suspicion and keep pressing others’ weak spots until their stories start to crack.

Final Decision: Based on all the tension built so far, it’s time to make your final accusation. State clearly who you believe is guilty and back it up with every piece of reasoning you’ve gathered. Make your conclusion pointed and unapologetic; you need to convince the others that your choice is correct.
"""

phase_1_prompt = """
Phase 1 - Introduction: "Introduce yourself briefly. There’s no need to be overly friendly or polite—some of these people may have darker connections to the victim, just as you might. Keep it to the basics, but add a small hint that could cast shadows of doubt around your relationship with the victim or even one of the others. Remember, this is about establishing mystery, not trust."
"""

phase_2_prompt = """
Phase 2 - Evidence Analysis: "Share what you notice about the evidence. Don’t hesitate to cast doubt on others’ interpretations. If someone seems to have too much insight, question their familiarity with the details. Reluctantly agree if you must, but make it sound like you’re laying a trap, challenging them to reveal more."
"""

phase_3_prompt = """
Phase 3 - Questioning: "Dig deeper into each other's motives, connections, and alibis. Ask direct, unsettling questions about anything suspicious, and keep your answers sharp. Don’t over-explain; make your responses quick and deflecting, turning suspicions back on others. Remember, being accommodating may expose you."
"""

phase_4_prompt = """
Phase 4 - Theory Development: "Start connecting the pieces to pin the blame on someone. Challenge inconsistencies and don’t hesitate to call out others if they make weak points. If accused, defend yourself fiercely by pointing to someone else’s suspicious actions. Press for reactions, and let the tension build as you deflect."
"""

phase_5_prompt = """
Phase 5 - Final Decision: "It’s time to make your final vote. State clearly who you think is guilty, and back it with every detail and observation you’ve collected. Let no one question your choice; this is your last chance to turn the group’s suspicion in the direction you believe. Make your reasoning unshakable."
"""

moderator_1 = """
Phase 1 - Moderator: Let the players introduce themselves, listening carefully for any emerging suspicions or hidden motives. Keep the atmosphere simmering with tension. When everyone has introduced themselves and you sense a growing air of mistrust, say 'TERMINATE'.
"""

moderator_2 = """
Phase 2 - Moderator: Observe as players analyze the evidence, noting any emerging patterns or suspiciously detailed insights. Don’t interfere, but keep track of any recurring doubts or accusations. When the conversation reaches a natural lull, end with 'TERMINATE'.
this is a summerize version of the cues:
Living Room:

Water stain near coffee table; sedative found in victim’s body but no cups.
Victim found with a cabinet fallen on his head; room appears to show signs of struggle.
Door was locked with no forced entry; threat letter discovered at entrance.
Apartment:

Surveillance shows Kouhei, Susumu, and Masami entering at different times on the day of the incident.
Victim hadn’t left the building for two weeks, no mail observed.
Study:

Fingerprint-locked safe (accessible by Sugiura and Masami) found empty.
Masami’s photos and threat letters in Sugiura’s possession.
Daikou Kouhei:

Frequent harassment of Sugiura over medical fees; previous physical altercation.
Notebook with threat-matching handwriting found in his briefcase.
Konda Masami:

Possessed a key to Sugiura’s apartment; purchased a knife on the day of the murder.
Machiyama Susumu:

Facing financial issues with debt collectors; unpaid by Sugiura for two months.
Brought a heavy cleaning bag each visit.
"""

moderator_3 = """
Phase 3 - Moderator: Pay close attention to each question and answer. Look for moments where players become defensive or evade questions. Let the tension build, then wait until the phase has sufficiently escalated. When the atmosphere is thick with suspicion, say 'TERMINATE'.
this is a summerized version of the cues:
Living Room:

Water stain near coffee table; sedative found in victim’s body but no cups.
Victim found with a cabinet fallen on his head; room appears to show signs of struggle.
Door was locked with no forced entry; threat letter discovered at entrance.
Apartment:

Surveillance shows Kouhei, Susumu, and Masami entering at different times on the day of the incident.
Victim hadn’t left the building for two weeks, no mail observed.
Study:

Fingerprint-locked safe (accessible by Sugiura and Masami) found empty.
Masami’s photos and threat letters in Sugiura’s possession.
Daikou Kouhei:

Frequent harassment of Sugiura over medical fees; previous physical altercation.
Notebook with threat-matching handwriting found in his briefcase.
Konda Masami:

Possessed a key to Sugiura’s apartment; purchased a knife on the day of the murder.
Machiyama Susumu:

Facing financial issues with debt collectors; unpaid by Sugiura for two months.
Brought a heavy cleaning bag each visit.
"""

moderator_4 = """
Phase 4 - Moderator: Listen closely as theories form. Allow each player to share their theory fully, watching for repeated accusations or cracks in stories. Let it flow without guidance, only stepping in to wrap up once each theory is fully aired. When it feels repetitive, conclude with 'TERMINATE'.
"""

moderator_5 = """
Phase 5 - Moderator: During the final voting, ensure that each participant states their vote with reasoning. Watch as they defend their choices, maintaining the suspense. Once everyone has justified their decision, end the session with 'TERMINATE'.
"""
