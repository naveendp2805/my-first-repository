import pygame as py
import sys
from datetime import datetime

py.init()

screen=py.display.set_mode((1300,700))
py.display.set_caption("astrology")

# fonts
font = py.font.Font('Avenir.ttf', 20)

# Input variables
birth_date = ""
birth_time = ""
birth_location = ""
active_input = None

# Results storage
result_text = ""

# Create rectangles for the input fields
input_boxes = {
    "date": py.Rect(400, 50, 300, 40),  # Positioning the rectangle next to the label
    "time": py.Rect(400, 120, 300, 40),  # For time input
    "location": py.Rect(400, 190, 300, 40)  # For location input
}
active_boxes = {key: False for key in input_boxes.keys()}

# Function to calculate Western Zodiac sign
def calculate_western_zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius", "(Kumbha)"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces", "(Meena)"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries", "(Mesha)"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus", "(Vrishabha)"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini", "(Mithuna)"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer", "(Kataka)"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo", "(Simha)"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo", "(Kanya)"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra", "(Tula)"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio", "(Vrishchika)"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius", "(Dhanus)"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn", "(Makara)"

# Function to calculate Chinese Zodiac sign
def calculate_chinese_zodiac_sign(year):
    signs = [
        ("Monkey", " (Kuruparamu)"),
        ("Rooster", " (Muthadi)"),
        ("Dog", " (Kukka)"),
        ("Pig", " (Pandi)"),
        ("Rat", " (Eluka)"),
        ("Ox", " (Vasha)"),
        ("Tiger", " (Puli)"),
        ("Rabbit", " (Kundelu)"),
        ("Dragon", " (Dragon)"),
        ("Snake", " (Paamu)"),
        ("Horse", " (Gaja)"),
        ("Goat", " (Pashuvu)")
    ]
    return signs[year % 12]

# Function to get zodiac descriptions
def get_zodiac_description(sign, zodiac_type):
    descriptions = {
        "Western": {
            "Aquarius": "Aquarius is known for being independent, inventive, and forward-thinking.",
            "Pisces": "Pisces are intuitive, compassionate, and artistic.",
            "Aries": "Aries is known for their energetic, confident, and adventurous nature.",
            "Taurus": "Taurus is practical, reliable, and patient.",
            "Gemini": "Gemini is adaptable, curious, and communicative.",
            "Cancer": "Cancer is nurturing, emotional, and protective.",
            "Leo": "Leo is charismatic, confident, and creative.",
            "Virgo": "Virgo is analytical, meticulous, and practical.",
            "Libra": "Libra is diplomatic, charming, and fair-minded.",
            "Scorpio": "Scorpio is passionate, determined, and resourceful.",
            "Sagittarius": "Sagittarius is adventurous, optimistic, and philosophical.",
            "Capricorn": "Capricorn is disciplined, ambitious, and practical."
        },
        "Chinese": {
            "Monkey": "People born in the Year of the Monkey are intelligent, witty, and energetic.",
            "Rooster": "Roosters are hardworking, confident, and courageous.",
            "Dog": "People born in the Year of the Dog are loyal, honest, and protective.",
            "Pig": "Pigs are compassionate, generous, and diligent.",
            "Rat": "Rats are clever, resourceful, and adaptable.",
            "Ox": "Oxen are reliable, patient, and methodical.",
            "Tiger": "Tigers are brave, competitive, and unpredictable.",
            "Rabbit": "Rabbits are gentle, compassionate, and elegant.",
            "Dragon": "Dragons are ambitious, charismatic, and energetic.",
            "Snake": "Snakes are intelligent, wise, and enigmatic.",
            "Horse": "Horses are energetic, independent, and charismatic.",
            "Goat": "Goats are gentle, creative, and compassionate."
        }
    }
    return descriptions[zodiac_type].get(sign, "No description available.")

# Function to get astrology info
def get_astrology_info():
    global result_text
    try:
        # Parse the date and time
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
        month = birth_datetime.month
        day = birth_datetime.day
        year = birth_datetime.year

        # Calculate zodiac signs
        western_sign, telugu_western = calculate_western_zodiac_sign(month, day)
        chinese_sign, telugu_chinese = calculate_chinese_zodiac_sign(year)

        # Get descriptions
        western_description = get_zodiac_description(western_sign, "Western")
        chinese_description = get_zodiac_description(chinese_sign, "Chinese")

        # Generate result text
        result_text = (f"Your Western Zodiac Sign: {western_sign} ({telugu_western})\n"
                       f"Characteristics: {western_description}\n\n"
                       f"Your Chinese Zodiac Sign: {chinese_sign} ({telugu_chinese})\n"
                       f"Characteristics: {chinese_description}\n")
    except ValueError:
        result_text = "Invalid input! Please enter the input in the correct format."

# Main game loop
running = True
while running:
    screen.fill("grey")

    # Draw input labels and rectangles
    date_label = font.render("Birth Date (DD-MM-YYYY):", True, "black")
    screen.blit(date_label, (50, 55))  # Display label
    py.draw.rect(screen, "chartreuse" if active_boxes["date"] else "white", input_boxes["date"], 2)

    time_label = font.render("Birth Time (HH:MM):", True, "black")
    screen.blit(time_label, (50, 125))  # Display label
    py.draw.rect(screen, "chartreuse" if active_boxes["time"] else "white", input_boxes["time"], 2)

    location_label = font.render("Birth Location:", True, "black")
    screen.blit(location_label, (50, 195))  # Display label
    py.draw.rect(screen, "chartreuse" if active_boxes["location"] else "white", input_boxes["location"], 2)

    # Render the input texts inside the rectangles
    date_text = font.render(birth_date, True, "black")
    screen.blit(date_text, (input_boxes["date"].x + 10, input_boxes["date"].y + 5))

    time_text = font.render(birth_time, True, "black")
    screen.blit(time_text, (input_boxes["time"].x + 10, input_boxes["time"].y + 5))

    location_text = font.render(birth_location, True, "black")
    screen.blit(location_text, (input_boxes["location"].x + 10, input_boxes["location"].y + 5))

    # Draw the result text
    if result_text:
        y_offset = 250
        for line in result_text.split("\n"):
            result_display = font.render(line, True, "blue")
            screen.blit(result_display, (50, y_offset))
            y_offset += 30

    # Event handling
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            for key, box in input_boxes.items():
                if box.collidepoint(event.pos):
                    active_input = key
                    active_boxes = {k: False for k in input_boxes.keys()}
                    active_boxes[key] = True
        elif event.type == py.KEYDOWN:
            if event.key == py.K_BACKSPACE:
                if active_input == "date" and len(birth_date) > 0:
                    birth_date = birth_date[:-1]
                elif active_input == "time" and len(birth_time) > 0:
                    birth_time = birth_time[:-1]
                elif active_input == "location" and len(birth_location) > 0:
                    birth_location = birth_location[:-1]
            elif event.key == py.K_RETURN:
                get_astrology_info()
            else:
                if active_input == "date":
                    birth_date += event.unicode
                elif active_input == "time":
                    birth_time += event.unicode
                elif active_input == "location":
                    birth_location += event.unicode

    py.display.flip()

py.quit
