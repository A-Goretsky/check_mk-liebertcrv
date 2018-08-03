def perfometer_liebertcrv_air_temp(row, check_command, perf_data):
    # Perfdata Tuple Format
    # ("temp", supp_temp, supp_warn, supp_crit, min, max)

    if row['service_description'] == "Air Temperature Control Sensor":
        return "", ""

    else:
        color = { 0: "#80ff20", 1: "#ffdf00", 2: "#ff0033", 3: "#ff8020" }[row["service_state"]]
        val = perf_data[0][1]
        total = perf_data[0][6]
        return "%f C" % (val), perfometer_linear(val * 100 / total, color)

# Add perfometer to perfometers dictionary.
perfometers['check_mk-liebertcrv_air_temp'] = perfometer_liebertcrv_air_temp
