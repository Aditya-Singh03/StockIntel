from flask import Blueprint, request, jsonify
from .fetch_news import fetch_news
from .analyze_news import analyze_news

api = Blueprint("api", __name__)

@api.route("/news", methods=["GET"])
def get_news():
    query = request.args.get("query")
    articles = fetch_news(query)
    return jsonify(articles)

@api.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    analysis = analyze_news(data["articles"])
    return jsonify({"analysis": analysis})