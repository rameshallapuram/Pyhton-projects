alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
   'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1 #to direct the shift
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char) #to extract the index of the input character.
      new_position = position + shift_amount #to shift the index in alphabet list.
      end_text += alphabet[new_position] #appending the char at the new shifted index in the list.
    else:
      end_text += char #for chars not in the list, they will be appended without alteration.
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

continue_program = True
while continue_program == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift % 26 
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Do you want to continue? 'yes' or 'no'").lower()
  if restart == "no":
    continue_program = False
    print("Thank You! Bye")
