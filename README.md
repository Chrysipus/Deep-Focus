# Deep Focus Logbook

A time logger to measure and promote deeply focused work/study habits

0. how to use it
1. What inspired it
2. What it's made of
3. Testing version

        
        
       Short version: *Download the Deep Focus Logbook.exe and optionally FocusLogbook.json from the main folder and enjoy!*

**0.** A little longer version:The Logbook has a chronometer. Use it for the duration of resolute attention only to one determined task, be it for studies, work or hobby. Stop it when te attention breaks either accidentally or deliberately. Attention in this context means not doing any other tasks (such as checking phone for messages). A little daydreaming can pass.
When the chronometer is stopped, it will add the time to your total times today. The total day's times can be compared to other days using the 'Chart' button. 
Only times above 23 minutes and 15 seconds (1395 seconds) will be logged. Anything less would hardly pass as deeply focused attention - studies indicate that our focus needs time to reach its peak. This limitation is intentional for educational purposes as well as to allow measuring specifically only the time that is spent focused and not many intervals of just a few minutes (otherwise the program might as well be called a Shallow Distractions Logbook).

The JSON file FocusLogbook.json is used to store daily times. You can download the provided file for testing purposes (the 'Chart' button will otherwise not work until you have at least two day's times.)

1. While studying Python at a Codeacademy, I was also reading Cal Newport's book 'Deep Work'. It prompted me to read more about the science behind attention. I found research done at California University that indicated full focus requires on average 23 minutes and 15 seconds ( https://www.themuse.com/advice/this-is-nuts-it-takes-nearly-30-minutes-to-refocus-after-you-get-distracted ).

  These discoveries made me want to spend time programming with better focus, cutting out any distractions. I wanted to measure that time efficiently to monitor my progress. I realized I could create something that could do it for me and this is how I began working on the Deep Focus Logbook. At first it was supposed to only be a chronometer, but then I decided to add additional functionality for better ability to analyse the focused times as well as to learn programming while doing this. 

2. The logbook is all made using Python 3.10.5 on VSC. The GUI is made using Tkinter. Pyinstaller was used to make .exe files. 

3. The testing version is the same as the non-testing one, except it records ALL times instead of being bound by the 1395 second restriction. It makes it less useful for the intended purpose of recording only the times of deep focus (and deep focus certainly requires time) but can be used to explore the features of the program.
