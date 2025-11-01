#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic Electrical Engineering Equations (Interactive CLI)

Variables (as requested):
I  = Amps
V  = Volts (RMS). For THREE-PHASE, use LINE-TO-LINE voltage (V_LL).
KVA = Kilo Volt-Amps (apparent power)
KW  = Kilo Watts (real power)
PF  = Power Factor (0–1)
W   = Watts (real power)

Formulas implemented:

Single-phase
------------
I   = (1000*KW) / (V*PF)
I   = (1000*KVA) / V
I   =  W / (V*PF)

KW  = (V*I*PF) / 1000            => W = V*I*PF
KVA = (V*I) / 1000               =>  VA = V*I

Three-phase (balanced, using line-to-line voltage V)
---------------------------------------------------
I   = (1000*KW) / (sqrt(3)*V*PF)
I   = (1000*KVA) / (sqrt(3)*V)
I   =  W / (sqrt(3)*V*PF)

KW  = (sqrt(3)*V*I*PF) / 1000    => W  = sqrt(3)*V*I*PF
KVA = (sqrt(3)*V*I) / 1000       => VA = sqrt(3)*V*I

Handy relations: KW = KVA * PF, and W = 1000*KW, VA = 1000*KVA
"""
from math import sqrt

SQRT3 = sqrt(3.0)

# ---------- Helper input utilities ----------
def ask_float(prompt, allow_zero=False, min_val=None, max_val=None):
    while True:
        s = input(prompt).strip()
        if s.lower() in {"q", "quit", "exit"}:
            raise KeyboardInterrupt
        try:
            x = float(s)
            if not allow_zero and x == 0.0:
                print("Value cannot be zero. Enter a non-zero value, or type 'q' to quit.")
                continue
            if min_val is not None and x < min_val:
                print(f"Value must be ≥ {min_val}. Try again, or type 'q' to quit.")
                continue
            if max_val is not None and x > max_val:
                print(f"Value must be ≤ {max_val}. Try again, or type 'q' to quit.")
                continue
            return x
        except ValueError:
            print("Please enter a valid number (or type 'q' to quit).")

def pretty_number(x):
    # Format numbers sensibly for engineering style outputs
    if abs(x) >= 100:
        return f"{x:,.2f}"
    elif abs(x) >= 1:
        return f"{x:,.4f}"
    else:
        return f"{x:.6f}"

def press_enter():
    input("\nPress Enter to continue...")

# ---------- Core equation functions ----------
# Amps (I)
def amps_single_from_kw(KW, V, PF):   return (1000.0*KW)/(V*PF)
def amps_single_from_kva(KVA, V):     return (1000.0*KVA)/V
def amps_single_from_w(W, V, PF):     return W/(V*PF)

def amps_three_from_kw(KW, V, PF):    return (1000.0*KW)/(SQRT3*V*PF)  # V is line-to-line
def amps_three_from_kva(KVA, V):      return (1000.0*KVA)/(SQRT3*V)
def amps_three_from_w(W, V, PF):      return W/(SQRT3*V*PF)

# Real Power (KW)
def kw_single(V, I, PF):              return (V*I*PF)/1000.0
def kw_three(V, I, PF):               return (SQRT3*V*I*PF)/1000.0

# Apparent Power (KVA)
def kva_single(V, I):                  return (V*I)/1000.0
def kva_three(V, I):                   return (SQRT3*V*I)/1000.0

# ---------- Menu handlers ----------
def menu_amps():
    while True:
        print("\n--- Calculate Amps (I) ---")
        print("1) Single-phase: from KW")
        print("2) Single-phase: from KVA")
        print("3) Single-phase: from W")
        print("4) Three-phase (V is LINE-TO-LINE): from KW")
        print("5) Three-phase (V is LINE-TO-LINE): from KVA")
        print("6) Three-phase (V is LINE-TO-LINE): from W")
        print("0) Back to main menu")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            return
        try:
            if choice == "1":
                KW = ask_float("Enter KW: ")
                V  = ask_float("Enter V (Volts): ")
                PF = ask_float("Enter PF (0–1): ", min_val=0.0, max_val=1.0)
                I  = amps_single_from_kw(KW, V, PF)
                print(f"\nI = {pretty_number(I)} A")
            elif choice == "2":
                KVA = ask_float("Enter KVA: ")
                V   = ask_float("Enter V (Volts): ")
                I   = amps_single_from_kva(KVA, V)
                print(f"\nI = {pretty_number(I)} A")
            elif choice == "3":
                W  = ask_float("Enter W (Watts): ")
                V  = ask_float("Enter V (Volts): ")
                PF = ask_float("Enter PF (0–1): ", min_val=0.0, max_val=1.0)
                I  = amps_single_from_w(W, V, PF)
                print(f"\nI = {pretty_number(I)} A")
            elif choice == "4":
                KW = ask_float("Enter KW: ")
                V  = ask_float("Enter V_LINE-TO-LINE (Volts): ")
                PF = ask_float("Enter PF (0–1): ", min_val=0.0, max_val=1.0)
                I  = amps_three_from_kw(KW, V, PF)
                print(f"\nI = {pretty_number(I)} A")
            elif choice == "5":
                KVA = ask_float("Enter KVA: ")
                V   = ask_float("Enter V_LINE-TO-LINE (Volts): ")
                I   = amps_three_from_kva(KVA, V)
                print(f"\nI = {pretty_number(I)} A")
            elif choice == "6":
                W  = ask_float("Enter W (Watts): ")
                V  = ask_float("Enter V_LINE-TO-LINE (Volts): ")
                PF = ask_float("Enter PF (0–1): ", min_val=0.0, max_val=1.0)
                I  = amps_three_from_w(W, V, PF)
                print(f"\nI = {pretty_number(I)} A")
            else:
                print("Invalid option.")
                continue
            press_enter()
        except KeyboardInterrupt:
            print("\nReturning to previous menu...")
            return

def menu_kw():
    while True:
        print("\n--- Calculate Real Power (KW) ---")
        print("1) Single-phase: from V, I, PF")
        print("2) Three-phase (V is LINE-TO-LINE): from V, I, PF")
        print("0) Back to main menu")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            return
        try:
            if choice == "1":
                V  = ask_float("Enter V (Volts): ")
                I  = ask_float("Enter I (Amps): ")
                PF = ask_float("Enter PF (0–1): ", min_val=0.0, max_val=1.0, allow_zero=True)
                KW = kw_single(V, I, PF)
                print(f"\nKW = {pretty_number(KW)} kW  (W = {pretty_number(KW*1000)} W)")
            elif choice == "2":
                V  = ask_float("Enter V_LINE-TO-LINE (Volts): ")
                I  = ask_float("Enter I (Amps): ")
                PF = ask_float("Enter PF (0–1): ", min_val=0.0, max_val=1.0, allow_zero=True)
                KW = kw_three(V, I, PF)
                print(f"\nKW = {pretty_number(KW)} kW  (W = {pretty_number(KW*1000)} W)")
            else:
                print("Invalid option.")
                continue
            press_enter()
        except KeyboardInterrupt:
            print("\nReturning to previous menu...")
            return

def menu_kva():
    while True:
        print("\n--- Calculate Apparent Power (KVA) ---")
        print("1) Single-phase: from V, I")
        print("2) Three-phase (V is LINE-TO-LINE): from V, I")
        print("0) Back to main menu")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            return
        try:
            if choice == "1":
                V   = ask_float("Enter V (Volts): ")
                I   = ask_float("Enter I (Amps): ")
                KVA = kva_single(V, I)
                print(f"\nKVA = {pretty_number(KVA)} kVA  (VA = {pretty_number(KVA*1000)} VA)")
            elif choice == "2":
                V   = ask_float("Enter V_LINE-TO-LINE (Volts): ")
                I   = ask_float("Enter I (Amps): ")
                KVA = kva_three(V, I)
                print(f"\nKVA = {pretty_number(KVA)} kVA  (VA = {pretty_number(KVA*1000)} VA)")
            else:
                print("Invalid option.")
                continue
            press_enter()
        except KeyboardInterrupt:
            print("\nReturning to previous menu...")
            return

def main_menu():
    while True:
        print("\n==============================")
        print(" Basic EE Equations Calculator")
        print("==============================")
        print("Note: For THREE-PHASE, V must be LINE-TO-LINE (V_LL).")
        print("\nChoose what to calculate:")
        print("1) Amps (I)")
        print("2) Real Power (KW)")
        print("3) Apparent Power (KVA)")
        print("q) Quit")
        choice = input("Your choice: ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        elif choice == "1":
            menu_amps()
        elif choice == "2":
            menu_kw()
        elif choice == "3":
            menu_kva()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")
