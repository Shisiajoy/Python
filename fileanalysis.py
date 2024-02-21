def main():
    user_input = input("Enter a file name (e.g., example.txt): ")   #prompt user to enter name of file
    try:
        with open(user_input, 'r') as input_file:       #to read contents of file
            content = input_file.read()
            print(content)
           
            num_lines = len(content.splitlines())    # Count lines
            print(f"Number of lines in the file: {num_lines}")

            
            num_words = len(content.split())        # Count words
            print(f"Number of words in the file: {num_words}")

            
            num_chars = len(content)        # Count characters (including whitespace)
            print(f"Number of characters in the file: {num_chars}")

            with open("analysis.txt", 'w') as output_file:          #writes analysis results to analysis.txt
                output_file.write(f"Number of lines: {num_lines}\n")
                output_file.write(f"Number of words: {num_words}\n")
                output_file.write(f"Number of characters: {num_chars}\n")
               

            print(f"Analysis results written to 'analysis.txt'.")  

    except FileNotFoundError:           #caters for non exixting file
        print(f"File '{user_input}' not found!")

    if __name__ == "__main__":      
    main()      #calling main function
