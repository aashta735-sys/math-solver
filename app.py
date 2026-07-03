import streamlit as st

st.set_page_config(page_title="Math Solver", page_icon="🧮")

st.title("🧮 Math Solver")

option = st.selectbox(
    "Choose an option",
    [
        "Basic Calculator",
        "Percentage Calculator",
        "Area Calculator",
        "Linear Equation Solver",
        "Quadratic Equation Solver"
    ]
)

if option == "Basic Calculator":
    n1 = st.number_input("First Number")
    op = st.selectbox("Operator", ["+", "-", "*", "/"])
    n2 = st.number_input("Second Number")
    if st.button("Calculate"):
        if op == "+":
            st.success(n1 + n2)
        elif op == "-":
            st.success(n1 - n2)
        elif op == "*":
            st.success(n1 * n2)
        elif op == "/":
            if n2 == 0:
                st.error("Zero Division Error")
            else:
                st.success(n1 / n2)

elif option == "Percentage Calculator":
    total = st.number_input("Total Value", min_value=0.0)
    obtained = st.number_input("Obtained Value", min_value=0.0)
    if st.button("Calculate Percentage"):
        if total == 0:
            st.error("Total cannot be zero")
        else:
            st.success(f"{(obtained/total)*100:.2f}%")

elif option == "Area Calculator":
    shape = st.selectbox("Shape", ["Square", "Rectangle", "Circle"])
    if shape == "Square":
        side = st.number_input("Side")
        if st.button("Area"):
            st.success(side * side)
    elif shape == "Rectangle":
        l = st.number_input("Length")
        b = st.number_input("Breadth")
        if st.button("Area"):
            st.success(l * b)
    else:
        r = st.number_input("Radius")
        if st.button("Area"):
            st.success(3.14159 * r * r)

elif option == "Linear Equation Solver":
    a = st.number_input("a")
    b = st.number_input("b")
    if st.button("Solve"):
        if a == 0:
            st.error("Invalid Equation")
        else:
            st.success(f"x = {-b/a}")

elif option == "Quadratic Equation Solver":
    a = st.number_input("a ")
    b = st.number_input("b ")
    c = st.number_input("c ")
    if st.button("Find Roots"):
        d = b*b - 4*a*c
        if a == 0:
            st.error("a cannot be zero")
        elif d >= 0:
            r1 = (-b + d**0.5)/(2*a)
            r2 = (-b - d**0.5)/(2*a)
            st.success(f"Root 1 = {r1}")
            st.success(f"Root 2 = {r2}")
        else:
            st.error("Complex Roots")
