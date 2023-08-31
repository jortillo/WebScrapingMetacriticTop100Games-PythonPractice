# WebScrapingMetacriticTop100Games-PythonPractice
Small project to practice and showcase python. Web scraping on metacritic and collected data from the top 100 games of all time.

## Tools Used
- Python
- Visual Studio Code

## Output
Output of top 100 games of all time. Collected data that included the name, platform, release date, and metascore of game. Data is scraped from metacritic and put into a dataframe using pandas. That dataframe is then generated into a csv file and using pandas to read csv file.
```
                                                             name          platform        release_date  metascore
0                            The Legend of Zelda: Ocarina of Time       Nintendo 64   November 23, 1998         99
1                                        Tony Hawk's Pro Skater 2       PlayStation  September 20, 2000         98
2                                             Grand Theft Auto IV     PlayStation 3      April 29, 2008         98
3                                                     SoulCalibur         Dreamcast   September 8, 1999         98
4                                             Grand Theft Auto IV          Xbox 360      April 29, 2008         98
5                                              Super Mario Galaxy               Wii   November 12, 2007         97
6                                            Super Mario Galaxy 2               Wii        May 23, 2010         97
7                                           Red Dead Redemption 2          Xbox One    October 26, 2018         97
8                                              Grand Theft Auto V          Xbox One   November 18, 2014         97
9                                              Grand Theft Auto V     PlayStation 3  September 17, 2013         97
10                                   Disco Elysium: The Final Cut                PC      March 30, 2021         97
11                                             Grand Theft Auto V          Xbox 360  September 17, 2013         97
12                                       Tony Hawk's Pro Skater 2         Dreamcast    November 6, 2000         97
13                        The Legend of Zelda: Breath of the Wild            Switch       March 3, 2017         97
14                                       Tony Hawk's Pro Skater 3     PlayStation 2    October 28, 2001         97
15                                                   Perfect Dark       Nintendo 64        May 22, 2000         97
16                                          Red Dead Redemption 2     PlayStation 4    October 26, 2018         97
17                                             Grand Theft Auto V     PlayStation 4   November 18, 2014         97
18                                                  Metroid Prime          GameCube   November 17, 2002         97
19                                           Grand Theft Auto III     PlayStation 2    October 22, 2001         97
20                                            Super Mario Odyssey            Switch    October 27, 2017         97
21                                           Halo: Combat Evolved              Xbox   November 14, 2001         97
22                                                        NFL 2K1         Dreamcast   September 7, 2000         97
23                                                    Half-Life 2                PC   November 16, 2004         96
24                                             Grand Theft Auto V                PC      April 13, 2015         96
25                        The Legend of Zelda: Breath of the Wild             Wii U       March 3, 2017         96
26                                                       BioShock          Xbox 360     August 21, 2007         96
27                                                  GoldenEye 007       Nintendo 64     August 25, 1997         96
28                                     Uncharted 2: Among Thieves     PlayStation 3    October 13, 2009         96
29                                                Resident Evil 4          GameCube    January 11, 2005         96
30                                                 The Orange Box          Xbox 360    October 10, 2007         96
31                                                 The Orange Box                PC    October 10, 2007         96
32                                            Batman: Arkham City     PlayStation 3    October 18, 2011         96
33                                                       Tekken 3       PlayStation      April 29, 1998         96
34                                                     Elden Ring     Xbox Series X   February 25, 2022         96
35                                                  Mass Effect 2          Xbox 360    January 26, 2010         96
36  The House in Fata Morgana - Dreams of the Revenants Edition -            Switch       April 9, 2021         96
37                         The Legend of Zelda: Twilight Princess          GameCube   December 11, 2006         96
38                                                Baldur's Gate 3                PC      August 3, 2023         96
39                                    The Elder Scrolls V: Skyrim          Xbox 360   November 11, 2011         96
40                                                      Half-Life                PC   November 19, 1998         96
41                                                     Elden Ring     PlayStation 5   February 25, 2022         96
42                                                Resident Evil 4     PlayStation 2    October 25, 2005         96
43                            The Legend of Zelda: The Wind Waker          GameCube      March 24, 2003         96
44                                                   Gran Turismo       PlayStation      April 30, 1998         96
45                      The Legend of Zelda: Tears of the Kingdom            Switch        May 12, 2023         96
46                                                       BioShock                PC     August 21, 2007         96
47                            Metal Gear Solid 2: Sons of Liberty     PlayStation 2   November 12, 2001         96
48                                   Grand Theft Auto Double Pack              Xbox    October 31, 2003         96
49                                    Portal Companion Collection            Switch       June 28, 2022         95
50                               Baldur's Gate II: Shadows of Amn                PC  September 24, 2000         95
51                                  Grand Theft Auto: San Andreas     PlayStation 2    October 26, 2004         95
52                                    Grand Theft Auto: Vice City     PlayStation 2    October 27, 2002         95
53                                                LittleBigPlanet     PlayStation 3    October 27, 2008         95
54                        The Legend of Zelda Collector's Edition          GameCube   November 17, 2003         95
55                                            Red Dead Redemption     PlayStation 3        May 18, 2010         95
56                                         Gran Turismo 3: A-Spec     PlayStation 2        July 9, 2001         95
57                                                         Halo 2              Xbox    November 9, 2004         95
58                                                Persona 5 Royal                PC    October 21, 2022         95
59                        The Legend of Zelda: A Link to the Past  Game Boy Advance    December 3, 2002         95
60                             The Legend of Zelda: Majora's Mask       Nintendo 64    October 25, 2000         95
61                                                 The Last of Us     PlayStation 3       June 14, 2013         95
62                         The Legend of Zelda: Twilight Princess               Wii   November 19, 2006         95
63                                                Madden NFL 2003     PlayStation 2     August 12, 2002         95
64                                       Tony Hawk's Pro Skater 2  Game Boy Advance        May 30, 2001         95
65                                                Persona 5 Royal     PlayStation 4      March 31, 2020         95
66                                      The Last of Us Remastered     PlayStation 4       July 29, 2014         95
67                                                       Portal 2                PC      April 18, 2011         95
68                                            Red Dead Redemption          Xbox 360        May 18, 2010         95
69                                                       Portal 2          Xbox 360      April 19, 2011         95
70                           Metal Gear Solid V: The Phantom Pain          Xbox One   September 1, 2015         95
71                                                       Portal 2     PlayStation 3      April 19, 2011         95
72                                       Tetris Effect: Connected            Switch     October 8, 2021         94
73                                                   World of Goo               Wii    October 13, 2008         94
74                                    The Elder Scrolls V: Skyrim                PC   November 10, 2011         94
75                                              BioShock Infinite     PlayStation 3      March 26, 2013         94
76                                               Final Fantasy IX       PlayStation   November 13, 2000         94
77                                 Call of Duty: Modern Warfare 2     PlayStation 3   November 10, 2009         94
78                                                     God of War     PlayStation 4      April 20, 2018         94
79                                       Tony Hawk's Pro Skater 4     PlayStation 2    October 23, 2002         94
80                                                  Devil May Cry     PlayStation 2    October 16, 2001         94
81                                 Call of Duty 4: Modern Warfare     PlayStation 3    November 5, 2007         94
82                                                Madden NFL 2002     PlayStation 2     August 19, 2001         94
83                                            Batman: Arkham City          Xbox 360    October 18, 2011         94
84                                       Metroid Prime Remastered            Switch    February 8, 2023         94
85                                                Persona 5 Royal     Xbox Series X    October 21, 2022         94
86                                                  Mass Effect 2                PC    January 26, 2010         94
87                        The Legend of Zelda: Ocarina of Time 3D               3DS       June 19, 2011         94
88                                                   Chrono Cross       PlayStation     August 15, 2000         94
89                                                        Celeste          Xbox One    January 26, 2018         94
90                                                       BioShock     PlayStation 3    October 21, 2008         94
91                                                  Mass Effect 2     PlayStation 3    January 17, 2011         94
92                                    Grand Theft Auto: Vice City                PC        May 12, 2003         94
93                                                Madden NFL 2004     PlayStation 2     August 12, 2003         94
94                                                   Gears of War          Xbox 360    November 7, 2006         94
95                                 The Elder Scrolls IV: Oblivion          Xbox 360      March 20, 2006         94
96                                                Persona 5 Royal            Switch    October 21, 2022         94
97                                    Sid Meier's Civilization II                PC   February 29, 1996         94
98                    The Witcher 3: Wild Hunt - Complete Edition     PlayStation 5   December 14, 2022         94
99                                                          Quake                PC       June 22, 1996         94
```
Output of average metascore from top 100 games by platform. Output is generated using pandas.melt.
```
            platform   variable      value
0          Dreamcast  metascore  97.333333
1        Nintendo 64  metascore  96.750000
2               Xbox  metascore  96.000000
3           GameCube  metascore  96.000000
4              Wii U  metascore  96.000000
5           Xbox One  metascore  95.750000
6                Wii  metascore  95.750000
7      PlayStation 4  metascore  95.600000
8        PlayStation  metascore  95.600000
9           Xbox 360  metascore  95.545455
10            Switch  metascore  95.375000
11                PC  metascore  95.200000
12     PlayStation 2  metascore  95.166667
13     PlayStation 3  metascore  95.153846
14     Xbox Series X  metascore  95.000000
15     PlayStation 5  metascore  95.000000
16  Game Boy Advance  metascore  95.000000
17               3DS  metascore  94.000000
```
## Data Visualization


Output of average metascore from top 100 games by platform visualized as a horizontal bar graph. Horizontal bar graph is generated through matplotlib
![Data Visualization](PlatformRankingsByMetascore.png)
