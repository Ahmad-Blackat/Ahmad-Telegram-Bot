import html
import io
import random
import time
from faker import Faker
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# ==========================================
# CONFIGURATION
# ==========================================
BOT_TOKEN = "8796581148:AAEvqkG5aT-XE1meR6jLFP6czw_t3cCJRQ4"
BOT_USERNAME = "@ahmad_info_17_bot"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# ==========================================
# SAFE EMOJI ENGINE
# ==========================================
E = {
    "rocket": "\U0001F680",
    "zap": "\u26A1",
    "sparkles": "\u2728",
    "fire": "\U0001F525",
    "pin": "\U0001F4CD",
    "postbox": "\U0001F4EE",
    "phone": "\U0001F4DE",
    "dna": "\U0001F9EC",
    "clip": "\U0001F4CB",
    "user": "\U0001F464",
    "globe": "\U0001F30D",
    "bulb": "\U0001F4A1",
    "refresh": "\U0001F504",
    "inbox": "\U0001F4E5",
    "back": "\U0001F519",
    "check": "\u2705",
    "cross": "\u274C",
    "warn": "\u26A0\uFE0F",
    "gear": "\u2699\uFE0F",
    "sat": "\U0001F4E1",
    "search": "\U0001F50D",
    "doc": "\U0001F4C4",
    "wave": "\U0001F44B",
    "point_d": "\U0001F447",
    "point_r": "\U0001F449",
    "man": "\U0001F468",
    "woman": "\U0001F469",
    "shield": "\U0001F6E1\uFE0F",
    "vip": "\U0001F48E",
    "bar_full": "\u2588",
    "bar_empty": "\u2591",
}

FLAGS = {
    "us": "\U0001F1FA\U0001F1F8",
    "pk": "\U0001F1F5\U0001F1F0",
    "uk": "\U0001F1EC\U0001F1E7",
    "ca": "\U0001F1E8\U0001F1E6",
    "au": "\U0001F1E6\U0001F1FA",
    "in": "\U0001F1EE\U0001F1F3",
    "de": "\U0001F1E9\U0001F1EA",
    "ae": "\U0001F1E6\U0001F1EA",
}

# ==========================================
# REAL-LOOKING SYNCHRONIZED GEO DATABASE
# ==========================================
COUNTRY_DB = {
    "us": {
        "name": "United States",
        "flag": FLAGS["us"],
        "locale": "en_US",
        "currency": "USD ($)",
        "locations": [
            {
                "city": "New York",
                "state": "NY",
                "state_full": "New York",
                "zip_prefix": "100",
                "area_codes": ["212", "646", "917"],
            },
            {
                "city": "Los Angeles",
                "state": "CA",
                "state_full": "California",
                "zip_prefix": "900",
                "area_codes": ["213", "310", "323"],
            },
            {
                "city": "Chicago",
                "state": "IL",
                "state_full": "Illinois",
                "zip_prefix": "606",
                "area_codes": ["312", "773"],
            },
            {
                "city": "Houston",
                "state": "TX",
                "state_full": "Texas",
                "zip_prefix": "770",
                "area_codes": ["713", "281", "832"],
            },
            {
                "city": "Miami",
                "state": "FL",
                "state_full": "Florida",
                "zip_prefix": "331",
                "area_codes": ["305", "786"],
            },
            {
                "city": "Seattle",
                "state": "WA",
                "state_full": "Washington",
                "zip_prefix": "981",
                "area_codes": ["206"],
            },
            {
                "city": "Dallas",
                "state": "TX",
                "state_full": "Texas",
                "zip_prefix": "752",
                "area_codes": ["214", "469", "972"],
            },
            {
                "city": "Atlanta",
                "state": "GA",
                "state_full": "Georgia",
                "zip_prefix": "303",
                "area_codes": ["404", "678", "770"],
            },
        ],
    },
    "pk": {
        "name": "Pakistan",
        "flag": FLAGS["pk"],
        "locale": "en_US",
        "currency": "PKR (Rs)",
        "first_names_m": [
            "Ahmad",
            "Muhammad",
            "Ali",
            "Hassan",
            "Usman",
            "Bilal",
            "Zain",
            "Hamza",
            "Fahad",
            "Saad",
            "Taha",
            "Arslan",
            "Haris",
            "Rizwan",
        ],
        "first_names_f": [
            "Ayesha",
            "Fatima",
            "Zainab",
            "Maryam",
            "Sana",
            "Hira",
            "Noor",
            "Laiba",
            "Mahnoor",
            "Iqra",
            "Anum",
            "Momina",
            "Khadija",
        ],
        "last_names": [
            "Khan",
            "Malik",
            "Sheikh",
            "Raza",
            "Qureshi",
            "Chaudhry",
            "Butt",
            "Hashmi",
            "Siddiqui",
            "Mirza",
            "Javed",
            "Iqbal",
            "Abbasi",
            "Gillani",
            "Bhatti",
        ],
        "streets": [
            "Main Boulevard, Gulberg III",
            "Phase 6, DHA",
            "Johar Town, Block G",
            "Model Town, Link Road",
            "Clifton Block 5",
            "PECHS Block 2",
            "F-7 Markaz, Jinnah Super",
            "G-11/3, Street 14",
            "Bahria Town Phase 4",
            "Satellite Town, Block B",
            "Cantt Area, Mall Road",
            "Wapda Town, Phase 1",
        ],
        "locations": [
            {"city": "Lahore", "state": "Punjab", "zip": "54000"},
            {"city": "Lahore", "state": "Punjab", "zip": "54660"},
            {"city": "Karachi", "state": "Sindh", "zip": "75500"},
            {"city": "Karachi", "state": "Sindh", "zip": "74400"},
            {
                "city": "Islamabad",
                "state": "Islamabad Capital Territory",
                "zip": "44000",
            },
            {"city": "Rawalpindi", "state": "Punjab", "zip": "46000"},
            {"city": "Faisalabad", "state": "Punjab", "zip": "38000"},
            {"city": "Multan", "state": "Punjab", "zip": "60000"},
            {"city": "Peshawar", "state": "Khyber Pakhtunkhwa", "zip": "25000"},
        ],
    },
    "uk": {
        "name": "United Kingdom",
        "flag": FLAGS["uk"],
        "locale": "en_GB",
        "currency": "GBP (£)",
        "locations": [
            {"city": "London", "state": "England", "zip_prefix": "SW1A"},
            {"city": "Manchester", "state": "England", "zip_prefix": "M1"},
            {"city": "Birmingham", "state": "England", "zip_prefix": "B1"},
            {"city": "Edinburgh", "state": "Scotland", "zip_prefix": "EH1"},
            {"city": "Glasgow", "state": "Scotland", "zip_prefix": "G1"},
            {"city": "Liverpool", "state": "England", "zip_prefix": "L1"},
        ],
    },
    "ca": {
        "name": "Canada",
        "flag": FLAGS["ca"],
        "locale": "en_CA",
        "currency": "CAD ($)",
        "locations": [
            {"city": "Toronto", "state": "Ontario (ON)", "zip_prefix": "M5V"},
            {
                "city": "Vancouver",
                "state": "British Columbia (BC)",
                "zip_prefix": "V6B",
            },
            {"city": "Montreal", "state": "Quebec (QC)", "zip_prefix": "H2Y"},
            {"city": "Calgary", "state": "Alberta (AB)", "zip_prefix": "T2P"},
            {"city": "Ottawa", "state": "Ontario (ON)", "zip_prefix": "K1P"},
        ],
    },
    "au": {
        "name": "Australia",
        "flag": FLAGS["au"],
        "locale": "en_AU",
        "currency": "AUD ($)",
        "locations": [
            {"city": "Sydney", "state": "New South Wales", "zip": "2000"},
            {"city": "Melbourne", "state": "Victoria", "zip": "3000"},
            {"city": "Brisbane", "state": "Queensland", "zip": "4000"},
            {"city": "Perth", "state": "Western Australia", "zip": "6000"},
        ],
    },
    "in": {
        "name": "India",
        "flag": FLAGS["in"],
        "locale": "en_IN",
        "currency": "INR (Rs)",
        "locations": [
            {"city": "Mumbai", "state": "Maharashtra", "zip": "400001"},
            {"city": "New Delhi", "state": "Delhi", "zip": "110001"},
            {"city": "Bengaluru", "state": "Karnataka", "zip": "560001"},
            {"city": "Hyderabad", "state": "Telangana", "zip": "500001"},
        ],
    },
    "de": {
        "name": "Germany",
        "flag": FLAGS["de"],
        "locale": "de_DE",
        "currency": "EUR (Euro)",
        "locations": [
            {"city": "Berlin", "state": "Berlin", "zip": "10115"},
            {"city": "Munich", "state": "Bavaria", "zip": "80331"},
            {"city": "Frankfurt", "state": "Hesse", "zip": "60311"},
            {"city": "Hamburg", "state": "Hamburg", "zip": "20095"},
        ],
    },
    "ae": {
        "name": "United Arab Emirates",
        "flag": FLAGS["ae"],
        "locale": "en_US",
        "currency": "AED",
        "first_names_m": [
            "Rashid",
            "Zayed",
            "Hamdan",
            "Tariq",
            "Omar",
            "Khalid",
        ],
        "first_names_f": ["Fatima", "Noora", "Mariam", "Reem"],
        "last_names": [
            "Al Maktoum",
            "Al Nahyan",
            "Al Qasimi",
            "Al Suwaidi",
            "Al Mansoori",
            "Al Hashimi",
            "Al Shamsi",
        ],
        "streets": [
            "Sheikh Zayed Road",
            "Jumeirah Beach Road",
            "Al Wasl Road, Downtown",
            "Corniche Road",
            "Al Rigga Street, Deira",
            "Dubai Marina Walk",
        ],
        "locations": [
            {"city": "Dubai", "state": "Emirate of Dubai", "zip": "00000"},
            {
                "city": "Abu Dhabi",
                "state": "Emirate of Abu Dhabi",
                "zip": "00000",
            },
            {"city": "Sharjah", "state": "Emirate of Sharjah", "zip": "00000"},
        ],
    },
}

LAST_GENERATED_CACHE = {}


def make_bar(filled, total=10):
  return E["bar_full"] * filled + E["bar_empty"] * (total - filled)


def generate_deep_profile(country_code):
  country_code = country_code.lower().strip()
  if country_code not in COUNTRY_DB:
    country_code = "us"

  c_info = COUNTRY_DB[country_code]
  fake = Faker(c_info["locale"])
  loc = random.choice(c_info["locations"])

  gender = random.choice(["Male", "Female"])
  gender_icon = E["man"] if gender == "Male" else E["woman"]

  if country_code in ["pk", "ae"]:
    fname = random.choice(
        c_info["first_names_m"]
        if gender == "Male"
        else c_info["first_names_f"]
    )
    lname = random.choice(c_info["last_names"])
  else:
    fname = (
        fake.first_name_male() if gender == "Male" else fake.first_name_female()
    )
    lname = fake.last_name()

  if country_code == "us":
    street_suffix = random.choice(["St", "Ave", "Blvd", "Dr", "Ln"])
    addr1v8g9unxthf22fsjfjg5l9yxf5g0jldjg5k92nupfzu6a3jq8lfxs4
    apt_letter = random.choice(["A", "B", "C"])
    addr2 = random.choice([
        f"Apt. {random.randint(1, 99)}{apt_letter}",
        f"Suite {random.randint(100, 800)}",
        f"Unit {random.randint(1, 50)}",
    ])
    city = loc["city"]
    state = f"{loc['state_full']} ({loc['state']})"
    postal = f"{loc['zip_prefix']}{random.randint(10, 99)}"
    area = random.choice(loc["area_codes"])
    phone = f"+1 ({area}) {random.randint(200, 999)}-{random.randint(1000, 9999)}"

  elif country_code == "pk":
    street_choice = random.choice(c_info["streets"])
    addr1v8g9unxthf22fsjfjg5l9yxf5g0jldjg5k92nupfzu6a3jq8lfxs4
    addr2 = random.choice([
        "Floor 1",
        "Floor 2, Near Main Masjid",
        "Ground Portion",
        "Sector B, Corner Plot",
    ])
    city = loc["city"]
    state = loc["state"]
    postal = str(int(loc["zip"]) + random.randint(0, 90))
    prefix = random.choice([
        "300",
        "301",
        "302",
        "312",
        "315",
        "321",
        "322",
        "333",
        "334",
        "345",
    ])
    phone = f"+92 {prefix} {random.randint(1000000, 9999999)}"

  elif country_code == "uk":
    addr1v8g9unxthf22fsjfjg5l9yxf5g0jldjg5k92nupfzu6a3jq8lfxs4
    addr2 = f"Flat {random.randint(1, 30)}"
    city = loc["city"]
    state = loc["state"]
    uk_code = random.choice(["AA", "AB", "BD", "DX", "WT"])
    postal = f"{loc['zip_prefix']} {random.randint(1, 9)}{uk_code}"
    phone = (
        f"+44 7{random.randint(400, 999)} {random.randint(100000, 999999)}"
    )

  elif country_code == "ca":
    addr1v8g9unxthf22fsjfjg5l9yxf5g0jldjg5k92nupfzu6a3jq8lfxs4
    addr2 = f"Unit {random.randint(101, 1200)}"
    city = loc["city"]
    state = loc["state"]
    ca_let = random.choice(["A", "B", "C", "E", "G"])
    postal = f"{loc['zip_prefix']} {random.randint(1, 9)}{ca_let}{random.randint(1, 9)}"
    ca_area = random.choice(["416", "604", "514", "403"])
    phone = f"+1 ({ca_area}) {random.randint(200, 999)}-{random.randint(1000, 9999)}"

  elif country_code == "ae":
    ae_street = random.choice(c_info["streets"])
    addr1v8g9unxthf22fsjfjg5l9yxf5g0jldjg5k92nupfzu6a3jq8lfxs4
    ae_tower = random.choice(["A", "B", "C"])
    addr2 = f"Tower {ae_tower}, Flat {random.randint(101, 2405)}"
    city = loc["city"]
    state = loc["state"]
    postal = f"P.O. Box {random.randint(10000, 99999)}"
    ae_pref = random.choice(["0", "2", "5", "6"])
    phone = f"+971 5{ae_pref} {random.randint(100, 999)} {random.randint(1000, 9999)}"

  else:
    addr1v8g9unxthf22fsjfjg5l9yxf5g0jldjg5k92nupfzu6a3jq8lfxs4
    addr2 = f"Apt {random.randint(1, 90)}"
    city = loc["city"]
    state = loc["state"]
    postal = str(int(loc["zip"]) + random.randint(1, 50))
    phone = fake.phone_number()

  dob_obj = fake.date_of_birth(minimum_age=19, maximum_age=48)
  dob = dob_obj.strftime("%d %b, %Y")
  age = 2026 - dob_obj.year

  clean_fn = fname.lower().replace(" ", "")
  clean_ln = lname.lower().replace(" ", "")
  username = f"{clean_fn}_{clean_ln}{random.randint(10, 99)}"
  email_domain = random.choice(
      ["gmail.com", "outlook.com", "yahoo.com", "icloud.com", "proton.me"]
  )
  email = f"{clean_fn}.{clean_ln}{random.randint(100, 999)}@{email_domain}"
  password = fake.password(
      length=12,
      special_chars=True,
      digits=True,
      upper_case=True,
      lower_case=True,
  )
  blood_group = random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+"])
  job = fake.job()
  height = (
      f"{random.randint(5, 6)}'{random.randint(1, 11)}\""
      f" ({random.randint(158, 188)} cm)"
  )
  weight = f"{random.randint(55, 92)} kg"

  return {
      "code": country_code,
      "country": c_info["name"],
      "flag": c_info["flag"],
      "currency": c_info["currency"],
      "fname": fname,
      "lname": lname,
      "gender": f"{gender} {gender_icon}",
      "dob": f"{dob} ({age} Years)",
      "addr1" : addr1,
      "addr2": addr2,
      "city": city,
      "state": state,
      "postal": postal,
      "phone": phone,
      "email": email,
      "username": username,
      "password": password,
      "blood": blood_group,
      "job": job,
      "height": height,
      "weight": weight,
  }


def format_profile_card(data):
  lines = [
      (
          f"<blockquote>{data['flag']} <b>DEEP IDENTITY & ADDRESS CARD"
          f" ({html.escape(data['country'].upper())})</b>"
          f" {data['flag']}</blockquote>"
      ),
      f"{E['user']} <b><u>PERSONAL PROFILE</u></b>",
      f"  <b>First Name:</b> <code>{html.escape(data['fname'])}</code>",
      f"  <b>Last Name:</b> <code>{html.escape(data['lname'])}</code>",
      f"  <b>Gender:</b> <code>{html.escape(data['gender'])}</code>",
      f"  <b>DOB:</b> <code>{html.escape(data['dob'])}</code>",
      (
          f"  <b>Blood / Height:</b> <code>{html.escape(data['blood'])} |"
          f" {html.escape(data['height'])}</code>\n"
      ),
      f"{E['pin']} <b><u>VERIFIED RESIDENTIAL ADDRESS</u></b>",
      f"  <b>Address Line 1:</b> <code>{html.escape(data['addr1'])}</code>",
      f"  <b>Address Line 2:</b> <code>{html.escape(data['addr2'])}</code>",
      f"  <b>City:</b> <code>{html.escape(data['city'])}</code>",
      f"  <b>State:</b> <code>{html.escape(data['state'])}</code>",
      f"  <b>Postal Code:</b> <code>{html.escape(data['postal'])}</code>",
      f"  <b>Phone No:</b> <code>{html.escape(data['phone'])}</code>\n",
      f"{E['globe']} <b><u>DIGITAL & WORK FOOTPRINT (BONUS)</u></b>",
      f"  <b>Email:</b> <code>{html.escape(data['email'])}</code>",
      f"  <b>Username:</b> <code>{html.escape(data['username'])}</code>",
      f"  <b>Password:</b> <code>{html.escape(data['password'])}</code>",
      f"  <b>Occupation:</b> <code>{html.escape(data['job'])}</code>",
      f"  <b>Currency:</b> <code>{html.escape(data['currency'])}</code>\n",
      (
          f"<blockquote>{E['bulb']} <i>Tip: Kisi bhi detail par 1 click (tap)"
          " karein, wo auto-copy ho jayegi!</i>"
      ),
      f"{E['zap']} <b>Information Generated By {BOT_USERNAME}</b></blockquote>",
  ]
  return "\n".join(lines)


def get_welcome_text(user_first):
  safe_name = html.escape(user_first or "User")
  lines = [
      (
          f"<blockquote>{E['sparkles']} <b>WELCOME TO AHMAD INFO BOT</b>"
          f" {E['sparkles']}</blockquote>"
      ),
      f"{E['wave']} Salam <b>{safe_name}</b>!",
      (
          "Welcome to the most advanced <b>Deep Fake Address & Identity"
          " Generator Bot</b> on Telegram.\n"
      ),
      f"{E['fire']} <b><u>PREMIUM FEATURES:</u></b>",
      f"  {E['pin']} 100% Realistic Street, City & State Match",
      f"  {E['postbox']} Valid & Synchronized Zip / Postal Codes",
      f"  {E['phone']} Country-Specific Area Code Phone Numbers",
      f"  {E['dna']} Deep Profile (DOB, Email, Pass, Blood, Job)",
      f"  {E['clip']} 1-Tap Copy & Instant .TXT File Export\n",
      (
          f"<blockquote>{E['point_d']} <b>Click an option below or use /fake"
          " command:</b>"
      ),
      f"{E['zap']} <b>Information Generated By {BOT_USERNAME}</b></blockquote>",
  ]
  return "\n".join(lines)


def get_start_keyboard():
  markup = InlineKeyboardMarkup(row_width=1)
  markup.add(
      InlineKeyboardButton(
          f"{E['zap']} Generate Fake Address + Profile {E['zap']}",
          callback_data="open_generator_menu",
      )
  )
  markup.row(
      InlineKeyboardButton(f"{FLAGS['us']} Quick US", callback_data="gen_us"),
      InlineKeyboardButton(f"{FLAGS['pk']} Quick PK", callback_data="gen_pk"),
      InlineKeyboardButton(f"{FLAGS['uk']} Quick UK", callback_data="gen_uk"),
  )
  markup.add(
      InlineKeyboardButton(
          f"{E['globe']} View All Supported Countries",
          callback_data="show_countries",
      )
  )
  return markup


def get_country_selector_keyboard():
  markup = InlineKeyboardMarkup(row_width=2)
  buttons = [
      InlineKeyboardButton(
          f"{FLAGS['us']} United States", callback_data="gen_us"
      ),
      InlineKeyboardButton(f"{FLAGS['pk']} Pakistan", callback_data="gen_pk"),
      InlineKeyboardButton(
          f"{FLAGS['uk']} United Kingdom", callback_data="gen_uk"
      ),
      InlineKeyboardButton(f"{FLAGS['ca']} Canada", callback_data="gen_ca"),
      InlineKeyboardButton(f"{FLAGS['au']} Australia", callback_data="gen_au"),
      InlineKeyboardButton(
          f"{FLAGS['ae']} UAE (Dubai)", callback_data="gen_ae"
      ),
      InlineKeyboardButton(f"{FLAGS['de']} Germany", callback_data="gen_de"),
      InlineKeyboardButton(f"{FLAGS['in']} India", callback_data="gen_in"),
  ]
  markup.add(*buttons)
  markup.add(
      InlineKeyboardButton(
          f"{E['back']} Back to Main Menu", callback_data="back_home"
      )
  )
  return markup


def get_result_action_keyboard(country_code):
  markup = InlineKeyboardMarkup(row_width=2)
  markup.add(
      InlineKeyboardButton(
          f"{E['refresh']} Generate New ({country_code.upper()})",
          callback_data=f"gen_{country_code}",
      ),
      InlineKeyboardButton(
          f"{E['globe']} Change Country", callback_data="show_countries"
      ),
  )
  markup.add(
      InlineKeyboardButton(
          f"{E['inbox']} Download Profile (.TXT)", callback_data="download_txt"
      )
  )
  return markup


def play_generation_animation(chat_id, country_code):
  c_info = COUNTRY_DB.get(country_code, COUNTRY_DB["us"])
  frames = [
      (
          f"{E['sat']} <b>Connecting to {c_info['flag']} {c_info['name']}"
          f" Server...</b>\n<code>[{make_bar(2)}] 20%</code>"
      ),
      (
          f"{E['search']} <b>Fetching Real Street, City & Postal"
          f" Records...</b>\n<code>[{make_bar(6)}] 60%</code>"
      ),
      (
          f"{E['dna']} <b>Synthesizing Deep Profile & Phone"
          f" Format...</b>\n<code>[{make_bar(9)}] 90%</code>"
      ),
      (
          f"{E['check']} <b>Identity Verified! Rendering"
          f" Card...</b>\n<code>[{make_bar(10)}] 100%</code>"
      ),
  ]

  msg = bot.send_message(chat_id, frames[0])
  for frame in frames[1:]:
    time.sleep(0.4)
    try:
      bot.edit_message_text(frame, chat_id, msg.message_id)
    except Exception:
      pass
  time.sleep(0.25)
  return msg.message_id


@bot.message_handler(commands=["start", "help"])
def handle_start(message):
  user_first = message.from_user.first_name or "User"
  anim_msg = bot.send_message(
      message.chat.id,
      f"{E['zap']} <b>Initializing Next-Gen Identity Engine...</b>",
  )
  time.sleep(0.4)

  welcome_text = get_welcome_text(user_first)
  try:
    bot.edit_message_text(
        welcome_text,
        message.chat.id,
        anim_msg.message_id,
        reply_markup=get_start_keyboard(),
    )
  except Exception:
    bot.send_message(
        message.chat.id, welcome_text, reply_markup=get_start_keyboard()
    )


@bot.message_handler(commands=["fake"])
def handle_fake_command(message):
  parts = message.text.split()

  if len(parts) < 2:
    lines = [
        f"<blockquote>{E['warn']} <b>HOW TO USE /fake COMMAND</b></blockquote>",
        "Please provide a country code with <code>/fake</code> command!\n",
        f"{E['pin']} <b><u>EXAMPLES:</u></b>",
        f"  {E['point_r']} <code>/fake us</code> (United States {FLAGS['us']})",
        f"  {E['point_r']} <code>/fake pk</code> (Pakistan {FLAGS['pk']})",
        (
            f"  {E['point_r']} <code>/fake uk</code> (United Kingdom"
            f" {FLAGS['uk']})"
        ),
        f"  {E['point_r']} <code>/fake ca</code> (Canada {FLAGS['ca']})",
        f"  {E['point_r']} <code>/fake ae</code> (UAE / Dubai {FLAGS['ae']})\n",
        f"{E['point_d']} <b>Or simply click a country button below:</b>",
    ]
    bot.reply_to(
        message,
        "\n".join(lines),
        reply_markup=get_country_selector_keyboard(),
    )
    return

  country_code = parts[1].lower().strip()
  if country_code not in COUNTRY_DB:
    err_msg = (
        f"{E['cross']} Country code <code>{html.escape(country_code)}</code>"
        f" not found!\n\n{E['check']} <b>Supported Codes:</b> <code>us</code>,"
        " <code>pk</code>, <code>uk</code>, <code>ca</code>, <code>au</code>,"
        " <code>ae</code>, <code>de</code>, <code>in</code>"
    )
    bot.reply_to(
        message, err_msg, reply_markup=get_country_selector_keyboard()
    )
    return

  msg_id = play_generation_animation(message.chat.id, country_code)
  data = generate_deep_profile(country_code)
  LAST_GENERATED_CACHE[message.chat.id] = data
  card_text = format_profile_card(data)

  bot.edit_message_text(
      card_text,
      message.chat.id,
      msg_id,
      reply_markup=get_result_action_keyboard(country_code),
  )


@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
  chat_id = call.message.chat.id
  data_cb = call.data

  if data_cb == "open_generator_menu":
    bot.answer_callback_query(call.id)
    lines = [
        (
            f"<blockquote>{E['vip']} <b>GENERATE FAKE ADDRESS + PROFILE</b>"
            f" {E['vip']}</blockquote>"
        ),
        f"{E['check']} <b>Use <code>/fake</code> command to use this feature!</b>",
        "Example: Type <code>/fake us</code> or <code>/fake pk</code> in chat.\n",
        f"{E['globe']} <b><u>AVAILABLE COUNTRY COMMANDS:</u></b>",
        f"  {FLAGS['us']} USA: <code>/fake us</code>",
        f"  {FLAGS['pk']} Pakistan: <code>/fake pk</code>",
        f"  {FLAGS['uk']} UK: <code>/fake uk</code>",
        f"  {FLAGS['ca']} Canada: <code>/fake ca</code>",
        f"  {FLAGS['au']} Australia: <code>/fake au</code>",
        f"  {FLAGS['ae']} UAE: <code>/fake ae</code>",
        f"  {FLAGS['de']} Germany: <code>/fake de</code>",
        f"  {FLAGS['in']} India: <code>/fake in</code>\n",
        (
            f"<blockquote>{E['point_d']} <i>Ya niche diye gaye buttons par"
            " direct click karein:</i>"
        ),
        (
            f"{E['zap']} <b>Information Generated By"
            f" {BOT_USERNAME}</b></blockquote>"
        ),
    ]
    bot.edit_message_text(
        "\n".join(lines),
        chat_id,
        call.message.message_id,
        reply_markup=get_country_selector_keyboard(),
    )

  elif data_cb == "show_countries":
    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        f"{E['globe']} <b>Select a Country below or type <code>/fake"
        " [code]</code>:</b>",
        chat_id,
        call.message.message_id,
        reply_markup=get_country_selector_keyboard(),
    )

  elif data_cb == "back_home":
    bot.answer_callback_query(call.id)
    user_first = call.from_user.first_name or "User"
    welcome_text = get_welcome_text(user_first)
    bot.edit_message_text(
        welcome_text,
        chat_id,
        call.message.message_id,
        reply_markup=get_start_keyboard(),
    )

  elif data_cb.startswith("gen_"):
    country_code = data_cb.split("_")[1]
    bot.answer_callback_query(
        call.id, f"Generating {country_code.upper()} Identity..."
    )

    c_info = COUNTRY_DB.get(country_code, COUNTRY_DB["us"])
    try:
      bot.edit_message_text(
          f"{E['gear']} <b>Generating {c_info['flag']} {c_info['name']} Deep"
          f" Profile...</b>\n<code>[{make_bar(7)}] 70%</code>",
          chat_id,
          call.message.message_id,
      )
      time.sleep(0.4)
    except Exception:
      pass

    profile_data = generate_deep_profile(country_code)
    LAST_GENERATED_CACHE[chat_id] = profile_data
    card_text = format_profile_card(profile_data)

    bot.edit_message_text(
        card_text,
        chat_id,
        call.message.message_id,
        reply_markup=get_result_action_keyboard(country_code),
    )

  elif data_cb == "download_txt":
    if chat_id not in LAST_GENERATED_CACHE:
      bot.answer_callback_query(
          call.id, "Please generate a profile first!", show_alert=True
      )
      return

    d = LAST_GENERATED_CACHE[chat_id]
    txt_lines = [
        "========================================",
        f"   DEEP IDENTITY & ADDRESS REPORT ({d['country'].upper()})",
        "========================================\n",
        f"First Name     : {d['fname']}",
        f"Last Name      : {d['lname']}",
        f"Gender         : {d['gender']}",
        f"DOB            : {d['dob']}",
        f"Address Line 1 : {d['addr1']}",
        f"Address Line 2 : {d['addr2']}",
        f"City           : {d['city']}",
        f"State          : {d['state']}",
        f"Postal Code    : {d['postal']}",
        f"Phone No       : {d['phone']}\n",
        "--- BONUS DIGITAL FOOTPRINT ---",
        f"Email          : {d['email']}",
        f"Username       : {d['username']}",
        f"Password       : {d['password']}",
        f"Occupation     : {d['job']}",
        f"Blood Group    : {d['blood']}",
        f"Height/Weight  : {d['height']} / {d['weight']}\n",
        "========================================",
        f"Information Generated By {BOT_USERNAME}",
        "========================================\n",
    ]
    txt_content = "\n".join(txt_lines)
    file_obj = io.BytesIO(txt_content.encode("utf-8"))
    file_obj.name = f"{d['fname']}_{d['lname']}_{d['code'].upper()}_Info.txt"

    bot.answer_callback_query(call.id, "Sending .TXT File...")
    caption_msg = (
        f"{E['doc']} <b>Full Profile Exported!</b>\n{E['zap']} <b>Information"
        f" Generated By {BOT_USERNAME}</b>"
    )
    bot.send_document(chat_id, file_obj, caption=caption_msg)


if __name__ == "__main__":
  print(f"{E['rocket']} {BOT_USERNAME} is now LIVE and running...")
  bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)