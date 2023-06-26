import webbrowser

url_9608 = "https://www.gceguide.com/papers/A Levels/Computer Science (for final examination in 2021) (9608)/"
url_9618 = "https://www.gceguide.com/papers/A Levels/Computer Science (for first examination in 2021) (9618)/"
# 9618_w21_ms_22.pdf
# 9618_y21_sm_3.pdf
# 9618/32/O/N/21
# 9618/03/SP/21

while True:
    pp_id = input("PP id: ").strip().split("/")
    if pp_id[0] == "9608":
        if pp_id[2] == "O":
            url = url_9608 + "20" + pp_id[4] + "/" + pp_id[0] + "_w" + pp_id[4] + "_ms_" + pp_id[1] + ".pdf"
        elif pp_id[2] == "M":
            url = url_9608 + "20" + pp_id[4] + "/" + pp_id[0] + "_s" + pp_id[4] + "_ms_" + pp_id[1] + ".pdf"
        elif pp_id[2] == "SP":
            url = url_9608 + "Specimen Papers"  + "/" + pp_id[0] + "_y" + pp_id[3] + "_sm_" + str(int(pp_id[1])) + ".pdf"

    elif pp_id[0] == "9618":
        if pp_id[2] == "O":
            url = url_9618 + "20" + pp_id[4] + "/" + pp_id[0] + "_w" + pp_id[4] + "_ms_" + pp_id[1] + ".pdf"
        elif pp_id[2] == "M":
            url = url_9618 + "20" + pp_id[4] + "/" + pp_id[0] + "_s" + pp_id[4] + "_ms_" + pp_id[1] + ".pdf"
        elif pp_id[2] == "SP":
            url = url_9618 + "Specimen Papers"  + "/" + pp_id[0] + "_y" + pp_id[3] + "_sm_" + str(int(pp_id[1])) + ".pdf"

    print(url)
    webbrowser.open(url)


