from flask import Flask, request, jsonify, render_template, Blueprint, Response, url_for

from app.service.map_service import get_all_terror_event_map, get_average_death_map, get_default_map

app_blueprint = Blueprint('map', __name__, )

@app_blueprint.route('/default_map', methods=['GET'])
def default_map():
    return jsonify({ 'map': get_default_map()._repr_html_() }), 200

@app_blueprint.route('/')
def index():
    return render_template('index.html')

@app_blueprint.route('/all-terror-event-map', methods=['POST'])
def all_terror_map():
    start_date = request.json.get('start_date')
    time_range = request.json.get("time_range")
    date_type = request.json.get("date_type")

    def is_all_params_valid():
        return all(param is not None for param in [time_range, start_date, date_type])

    try:
        if is_all_params_valid():
            res = get_all_terror_event_map(start_date=start_date, time_range=time_range, date_type=date_type)
        else:
            res = get_all_terror_event_map()

        return jsonify({ 'map':  res._repr_html_() }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app_blueprint.route('/average-death-map', methods=['POST'])
def average_death_map():
    try:
        top5 = True if request.json["top5"] else False

        res = get_average_death_map(top5)
        return jsonify({ 'map':  res._repr_html_() }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


