import webbrowser

user_term = input("What do you want to search for? ").replace(" ","+")

webbrowser.open(f"https://www.google.com/search?q={user_term}")

results = webbrowser.open(f"https://www.google.com/search?q={user_term}")

print(results)

print("Search completed.")