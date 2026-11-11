from flask import Flask, render_template, request

app = Flask(__name__)

city_data = {
    "hyderabad": {
        "name": "Hyderabad",
        "state": "Telangana",
        "description": "Hyderabad is famous for its history, IT industry and food.",
        "places": ["Charminar", "Golconda Fort", "Hussain Sagar"],
        "food": ["Hyderabadi Biryani", "Haleem"]
    },
    "vijayawada": {
        "name": "Vijayawada",
        "state": "Andhra Pradesh",
        "description": "Vijayawada is situated on the banks of Krishna River.",
        "places": ["Kanaka Durga Temple", "Prakasam Barrage", "Bhavani Island"],
        "food": ["Punugulu", "Andhra Meals"]
    },
    "bhimavaram": {
        "name": "Bhimavaram",
        "state": "Andhra Pradesh",
        "description": "Bhimavaram is known for its temples and aquaculture.",
        "places": ["Somaramam Temple", "Mavullamma Temple"],
        "food": ["Fish Curry", "Traditional Andhra Food"]
    },
    "palakollu": {
        "name": "Palakollu",
        "state": "Andhra Pradesh",
        "description": "Palakollu is a historic town in West Godavari district, famous for its temples and culture.",
        "places": ["Ksheera Ramalingeswara Swamy Temple", "Palakollu Temple Streets"],
        "food": ["Andhra Meals", "Traditional Sweets"]
    },
    "narsapur": {
        "name": "Narsapur",
        "state": "Andhra Pradesh",
        "description": "Narsapur is famous for its beautiful lace handicrafts and scenic surroundings.",
        "places": ["Narsapur Lace Park", "Godavari River Area"],
        "food": ["Andhra Fish Curry", "Prawn Biryani"]
    },
    "visakhapatnam": {
        "name": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "description": "Visakhapatnam is a beautiful coastal city known as the City of Destiny.",
        "places": ["RK Beach", "Kailasagiri", "Submarine Museum"],
        "food": ["Seafood", "Bamboo Chicken"]
    },
    "chennai": {
        "name": "Chennai",
        "state": "Tamil Nadu",
        "description": "Chennai is famous for its beaches, culture and industries.",
        "places": ["Marina Beach", "Kapaleeshwarar Temple", "Fort St George"],
        "food": ["Idli", "Dosa", "Filter Coffee"]
    },
    "bengaluru": {
        "name": "Bengaluru",
        "state": "Karnataka",
        "description": "Bengaluru is known as India's Silicon Valley.",
        "places": ["Lalbagh", "Bangalore Palace", "Cubbon Park"],
        "food": ["Masala Dosa", "Bisi Bele Bath"]
    },
    "mumbai": {
        "name": "Mumbai",
        "state": "Maharashtra",
        "description": "Mumbai is India's financial capital and a major entertainment centre.",
        "places": ["Gateway of India", "Marine Drive", "Elephanta Caves"],
        "food": ["Vada Pav", "Pav Bhaji"]
    },
    "delhi": {
        "name": "Delhi",
        "state": "Delhi",
        "description": "Delhi is India's capital and is famous for its historical monuments.",
        "places": ["India Gate", "Red Fort", "Qutub Minar"],
        "food": ["Chole Bhature", "Paratha"]
    },
    "kolkata": {
        "name": "Kolkata",
        "state": "West Bengal",
        "description": "Kolkata is known for its literature, art and cultural heritage.",
        "places": ["Victoria Memorial", "Howrah Bridge", "Dakshineswar Temple"],
        "food": ["Rasgulla", "Kathi Roll"]
    },
    "amaravati": {
        "name": "Amaravati",
        "state": "Andhra Pradesh",
        "description": "Amaravati is known for its Buddhist heritage and the Andhra Pradesh capital region.",
        "places": ["Amaravati Stupa", "Dhyana Buddha Statue"],
        "food": ["Andhra Meals", "Pulihora"]
    },
    "pune": {
        "name": "Pune",
        "state": "Maharashtra",
        "description": "Pune is famous for education, IT companies and historical forts.",
        "places": ["Shaniwar Wada", "Aga Khan Palace", "Sinhagad Fort"],
        "food": ["Misal Pav", "Puran Poli"]
    },
    "kochi": {
        "name": "Kochi",
        "state": "Kerala",
        "description": "Kochi is a beautiful coastal city known for its backwaters and culture.",
        "places": ["Fort Kochi", "Chinese Fishing Nets", "Mattancherry Palace"],
        "food": ["Appam", "Kerala Fish Curry"]
    },
    "jaipur": {
        "name": "Jaipur",
        "state": "Rajasthan",
        "description": "Jaipur is popularly known as the Pink City.",
        "places": ["Hawa Mahal", "Amber Fort", "City Palace"],
        "food": ["Dal Baati Churma", "Ghewar"]
    },
    "tirupati": {
        "name": "Tirupati",
        "state": "Andhra Pradesh",
        "description": "Tirupati is famous for the sacred Tirumala Venkateswara Temple.",
        "places": ["Tirumala Temple", "Sri Padmavathi Temple", "Kapila Theertham"],
        "food": ["Tirupati Laddu", "Andhra Meals"]
    },
    "warangal": {
        "name": "Warangal",
        "state": "Telangana",
        "description": "Warangal is known for its Kakatiya history and architecture.",
        "places": ["Warangal Fort", "Thousand Pillar Temple", "Ramappa Temple"],
        "food": ["Sarva Pindi", "Sakinalu"]
    },
    "rajahmundry": {
        "name": "Rajahmundry",
        "state": "Andhra Pradesh",
        "description": "Rajahmundry is a historic city located beside the Godavari River.",
        "places": ["Godavari Bridge", "Pushkar Ghat", "Dowleswaram Barrage"],
        "food": ["Pootharekulu", "Andhra Meals"]
    },
    "kakinada": {
        "name": "Kakinada",
        "state": "Andhra Pradesh",
        "description": "Kakinada is a coastal city known for its port and traditional sweets.",
        "places": ["Coringa Wildlife Sanctuary", "Hope Island", "Uppada Beach"],
        "food": ["Kakinada Kaja", "Seafood"]
    },
    "eluru": {
        "name": "Eluru",
        "state": "Andhra Pradesh",
        "description": "Eluru is a historic city known for its cultural heritage and handloom industry.",
        "places": ["Kolleru Lake", "Dwaraka Tirumala Temple"],
        "food": ["Andhra Meals", "Traditional Sweets"]
    }
}
@app.route("/", methods=["GET", "POST"])
def home():
    city = ""
    city_info = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        city_info = city_data.get(city.lower())

    return render_template(
        "index.html",
        city=city,
        city_info=city_info
    )


if __name__ == "__main__":
    app.run(debug=True)