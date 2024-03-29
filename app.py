from flask import Flask, render_template, request

def bidding_fees(bid):
    if bid >= 15000.00:
        return (bid * 0.0775)
    elif bid >= 12500.00  and bid <= 14999.99:
        return 890.0
    elif bid >= 12000.00 and bid <= 12499.99:
        return 875.00
    elif bid >= 11500.00 and bid <= 11999.99:
        return 860.00
    elif bid >= 11000.00 and bid <= 11499.99:
        return 845.00
    elif bid >= 10500.00 and bid <= 10999.99:
        return 830.00
    elif bid >= 10000.00 and bid <= 10499.99:
        return 815.00
    elif bid >= 7500.00 and bid <= 9999.99:
        return 785.00
    elif bid >= 7000.00 and bid <= 7499.99:
        return 775.00
    elif bid >= 6500.00 and bid <= 6999.99:
        return 750.00
    elif bid >= 6000.00 and bid <= 6499.99:
        return 750.00
    elif bid >= 5000.00 and bid <= 5999.99:
        return 750.00
    elif bid >= 4500.00 and bid <= 4999.99:
        return 700.00
    elif bid >= 4000.00 and bid <= 4499.99:
        return 690.00
    elif bid >= 3500.00 and bid <= 3999.99:
        return 675.00
    elif bid >= 3000.00 and bid <= 3499.99:
        return 650.00
    elif bid >= 2500.00 and bid <= 2999.99:
        return 550.00
    elif bid >= 2400.00 and bid <= 2499.99:
        return 525.00
    elif bid >= 2000.00 and bid <= 2399.99:
        return 500.00
    elif bid >= 1800.00 and bid <= 1999.99:
        return 465.00
    elif bid >= 1700.00 and bid <= 1799.99:
        return 450.00
    elif bid >= 1600.00 and bid <= 1699.99:
        return 440.00
    elif bid >= 1500.00 and bid <= 1599.99:
        return 420.00
    elif bid >= 1400.00 and bid <= 1499.99:
        return 410.00
    elif bid >= 1300.00 and bid <= 1399.99:
        return 400.00

def virtual_fees(bid):
    if bid >= 8000.00:
        return 149.00
    elif bid >= 6000 and bid <= 7999.99:
        return 139.00
    elif bid >= 4000 and bid <= 5999.99:
        return 109.00
    elif bid >= 2000.00 and bid <= 3999.99:
        return 99.00
    elif bid >= 1500.00 and bid <= 1999.99:
        return 89.00
    elif bid >= 1000.00 and bid <= 1499.99:
        return 79.00
    elif bid >= 500.00 and bid <= 999.99:
        return 59.00
    elif bid >= 100.00 and bid <= 499.99:
        return 49.00
    elif bid >= 0.00 and bid <= 99.99:
        return 0.00

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def calculate():
    gate_fee = 79
    env_fee = 10
    rate = 0.3879
    total = ''
    omr = ''
    if request.method == 'POST' and 'bid' in request.form:
        bid = float(request.form.get('bid'))

        total = bid + bidding_fees(bid) + virtual_fees(bid) + gate_fee + env_fee
        omr = round(total * rate)
    return render_template("index.html", total=total, omr=omr)

if __name__ == "__main__":
    app.run()
