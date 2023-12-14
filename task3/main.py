import word
import my_model
import random
import lwa
import numpy as np
import streamlit as st

# TO START PROGRAM TYPE: `streamlit run main.py`


def calculate(v, model):

    grades = [list(model['words'].keys())[random.randrange(0, 7)] for _ in range(50)] 

    h = min(item['lmf'][-1] for item in model['words'].values())
    m = 50
    intervals_umf = lwa.alpha_cuts_intervals(m)
    intervals_lmf = lwa.alpha_cuts_intervals(m, h)

    res_lmf = lwa.y_lmf(intervals_lmf, model, v)
    res_umf = lwa.y_umf(intervals_umf, model, v)
    res = lwa.construct_dit2fs(np.arange(*model['x']), intervals_lmf, res_lmf, intervals_umf, res_umf)

    sm = []
    model = my_model.words
    for title, fou in model['words'].items():
        sm.append((title, res.similarity_measure(word.Word(None, model['x'], fou['lmf'], fou['umf']))))
    res_word = max(sm, key=lambda item: item[1])

    return f"Result: {res_word}"

def main():
    st.title("Task 3")
    model = my_model.words
    values = []
    labels = list(model['words'].keys())
    for i in range(0, 7):
        field_name = f"| {labels[i]} | vote count"
        value = st.number_input(field_name, min_value=0, step=1)
        values.append(value)

    if st.button("Calculate"):
        result = calculate(values, model)
        st.success(result)


if __name__ == "__main__":
    # TO START PROGRAM TYPE: `streamlit run main.py`
    main()
