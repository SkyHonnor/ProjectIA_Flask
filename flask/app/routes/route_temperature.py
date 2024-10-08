from flask import Blueprint, render_template, request

temperature_page = Blueprint("temperature_page", __name__)

@temperature_page.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        degc = [-8.785, 1.611, 2.339, -0.146, -1.231e-2, -1.642e-2, 2.212e-3, 7.255e-4, -3.582e-6]
        degf = [-42.379, 2.049, 10.143, -0.225, -6.838e-3, -5.482e-2, 1.229e-3, 8.528e-4, -1.990e-6]
        temperature = int(request.form.get('temperature'))
        humidite = int(request.form.get('humidite'))
        indicedegc = degc[0] + degc[1] * temperature + degc[2] * humidite + degc[3] * temperature * humidite + degc[4] * (temperature ** 2) + degc[5] * (humidite ** 2) + degc[6] * (temperature ** 2) * humidite + degc[7] * temperature * (humidite ** 2) + degc[8] * (temperature ** 2) * (humidite ** 2)
        indicedegf = degf[0] + degf[1] * temperature + degf[2] * humidite + degf[3] * temperature * humidite + degf[4] * (temperature ** 2) + degf[5] * (humidite ** 2) + degf[6] * (temperature ** 2) * humidite + degf[7] * temperature * (humidite ** 2) + degf[8] * (temperature ** 2) * (humidite ** 2)
        return render_template('temperature/index.html', indicedegc=round(indicedegc,2), indicedegf=round(indicedegf,2), temperature=temperature, humidite=humidite)
    return render_template('temperature/index.html', temperature=36, humidite=70)