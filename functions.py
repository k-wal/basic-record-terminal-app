import os
import sys


def display_menu():
    os.system('clear')
    print("********************")
    print("    YOUR THOUGHTS   ")
    print("********************")
    print("\n\n")


def display_initial_choice():
    print("[1] See previous entries\n")
    print("[2] New entry\n")
    print("[q] Quit\n")
    return input("")


def show_entry_menu_choice():
    display_menu()
    print("[t] Today's entries\n")
    print("[m] This month's entries\n")
    print("[d] Another day's entries\n")
    print("[a] Another month's entries\n")
    print("[r] Entries of a range\n")
    print("[z] All previous entries\n")
    print("[b] Go back\n")
    print("[q] Quit")
    return input("")


def show_today_entries_choice():
    print("[a] Add an entry\n")
    print("[d] Delete an entry\n")
    print("[b] Go back\n")
    print("[h] Go home\n")
    print("[q] Quit\n")
    return input("")


def show_month_entries_choice():
    print("[d] Delete an entry\n")
    print("[b] Go back\n")
    print("[h] Go home\n")
    print("[q] Quit\n")
    return input("")
