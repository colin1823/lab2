def main():
    temperatures = []

    while True:
        try:
            temp = input("Enter a temperature (or type 'done' to finish): ")
            if temp.lower() == 'done':
                break
            temperatures.append(float(temp))
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

    if temperatures:
        print(f"Average Temperature: {sum(temperatures) / len(temperatures):.2f}")
        print(f"Minimum Temperature: {min(temperatures):.2f}")
        print(f"Maximum Temperature: {max(temperatures):.2f}")
    else:
        print("No temperatures were entered.")

if __name__ == "__main__":
    main()