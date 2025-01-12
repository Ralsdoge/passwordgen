# passwordgen
A very simple password generator to help with security on the internet. I was tired of coming up with terrible and insecure passwords based on random things in my life. Hope this helps some people, this only generates passwords it does not save any data.

A few notes that I would like to disclose about the generation file. When creating characters the random selection function uses random.sample so when selecting random characters it does not sample similar letters. This is more secure in my opinion as you dont get passwords like aka22@1b#. It really does happen with uncapped randomness. 

Its so annoying  when you find the perfect password and you are met with that terrible message, 'Password may not include ".","\","/",":","(",")"!'.
No More!
Now you can generate away those passwords with exclusion! Simply put in these illegal characters into the red box separated with commas like so: .,\,/,:,(,)
And receive passwords devoid of these characters!

When you are adjusting the sliders dont worry about them summing to 100. The program will add all of your slider values together and use that as the metaphorical 100% to calculate the percentage of types of characters to use. I did add a perf mode so you can add them to an evenly divisible total (Honestly I cant remember why I added it).

I also accounted for overflow conditions where if you select 100 numbers and 0 of the others you still receive a result. The program will repopulate the sample list if you have already used up the available characters in the selected character type. i.e 8901237465 then it resamples and begins fresh sampling each character again until length is satisfied.


Hope you find some use for this in complicated password debacles. - Ralsdoge
