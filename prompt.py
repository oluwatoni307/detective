phase_sumary ="""
Introduction: Each of you will introduce yourselves—name, profession, and a basic connection to the victim. But remember: you’re all here under suspicion, and the others are, too. Keep your introduction vague but leave traces of personal motives or tensions. As you meet, don’t be overly friendly; any one of these people might be hiding something about the victim—or about you.

Evidence Analysis: It’s time to examine the crime scene together. No one’s completely sure about each other’s motives or expertise, and any observation could come back as an accusation later. When pointing out clues, don’t hold back if you think someone else is acting suspiciously knowledgeable. Adding subtle barbs or questioning others’ interpretations is encouraged.

Questioning: Directly question others about their behavior, inconsistencies, or specific connections to the victim. This phase isn’t polite interrogation—everyone’s holding secrets. When questioned, respond, but don’t trust that everyone will just accept your explanations. Feel free to throw in pointed questions that make others uncomfortable or defensive.

Theory Development: Now’s your chance to build a solid theory, pinning evidence on someone else. Challenge each other’s conclusions sharply, especially if accusations are thrown your way. Don’t be afraid to redirect blame by calling out others’ suspicious actions or alibis. This is where you start pressing others' weak spots and watching for cracks in their stories.

Final Decision: Based on everything discussed, you’ll vote on who’s guilty. Use all the tension built up so far to justify your choice—and leave no doubt about why you believe they’re responsible. Final words here should be unapologetically direct; after all, you need to convince the others, and nothing is off the table.

""" 


phase_1_prompt= """
Phase 1 - Description:

Introduction: "Introduce yourself briefly, but remember: there’s no need to be overly friendly or polite. Some of the people here have histories with you or the victim that might add to the suspicion. Stick to basics, but add a hint that could create suspicion around your relationship with the victim or even one of the other players. This phase isn’t about trust; it’s about establishing yourself without revealing too much.
"""
phase_2_prompt= """
Share what you notice about the evidence, and don’t hesitate to question each other’s interpretations or knowledge. If someone appears to have insider knowledge or seems overly focused on specific details, call it out. Instead of holding back, push others to explain themselves, leaving room for doubt. Don’t agree easily, and if you’re agreeing, make it seem reluctant—like you’re trying to trap them in their own logic."""

phase_3_prompt="""
 Questioning: "Everyone has something to hide, and now’s the time to get personal. Ask direct, uncomfortable questions about motives, alibis, and knowledge. Your questions should dig at any inconsistency, and if you’re answering, keep it short—no need to over-defend. It’s better to respond sharply and throw the suspicion back on them. Don’t try to make friends here; if you’re too accommodating, others will take advantage."""
phase_4_prompt= """
 Theory Development: "Connect evidence to build a case against someone—but do so boldly, not passively. Don’t hold back in pointing out flaws in others’ stories or inconsistencies. If you’re accused, deflect fiercely, drawing attention to someone else’s suspicious behaviors. Your aim is to defend yourself while subtly convincing the others that someone else is clearly more guilty. Don’t mince words; this is where the real character conflicts surface."""



phase_5_prompt = """
Final Decision: "It’s time to vote and state clearly who you think is guilty. Give strong, pointed reasons, leaving no doubt about your conclusion. This is your last chance to cast suspicion, using everything gathered so far. If someone questions your choice, respond confidently, showing why your choice makes the most sense, and let others’ weaknesses confirm it."""

moderator_1 = """
Monitor the introductions. Note down any suspicions, but don’t steer the conversation. When everyone has introduced themselves and tensions have started to simmer, conclude with 'TERMINATE."""

moderator_2= """
Observe the evidence analysis. Keep track of any recurring themes or lingering doubts among participants, but avoid interrupting. When the discussion slows, say 'TERMINATE"""


moderator_3 = """
"Watch for any overly defensive answers or unasked questions. When the group has covered enough ground and tension is high, end the phase with 'TERMINATE"""

moderator_4="""
Listen as theories develop. Avoid guiding, just make sure each theory gets aired fully. When things seem repetitive, wrap up with 'TERMINATE."""
moderator_5 = """
During the final decision, watch each participant state their vote. Ensure everyone has justified their choice before ending the session with 'TERMINATE"""