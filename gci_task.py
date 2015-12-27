os = input("What do you use, Windows, Mac OS or Linux? ").lower().strip()
if os == "windows":
  print("You probably bought your computer from a store, or built your own.")
elif os == "mac os":
  print("You are using either an Apple Mac, or a hackintosh. It's illegal to sell the latter. ")
elif os == "linux":
  print("You probably have a multiboot setup. If not, you may not be able to use certain software. ")
else:
  print("I don't know what you're using.")