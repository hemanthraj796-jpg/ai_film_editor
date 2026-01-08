# This is a simple dictionary to help our AI 
# understand which file matches which script beat.

dataset = [
    {"shot": "shot1.mp4", "label": "Siri sitting at computer", "type": "Wide"},
    {"shot": "shot2.mp4", "label": "Dialogue: Why isn't this code working", "type": "Close-up"},
    {"shot": "shot3.mp4", "label": "Action: Hitting keyboard", "type": "Detail"}
]

print(f"Successfully mapped {len(dataset)} video clips to script beats.")