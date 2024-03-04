# The Problem with Wikipedia
It’s so difficult to find and extract tabular data from Wikipedia due to the total lack total lack of standardization and consistent formatting of Wikipedia’s list and category pages.
Here are just a few examples of list pages in which the relevant list items are formatted in wildly different ways, and my attempt at finding a standard for parsing them:

| Where are the list items? | Example list pages |
| ------------- | ------------- |
| col 3 is      | right-aligned |
| col 2 is      | centered      |
| zebra stripes | are neat      |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

Where are the list items? | Example list pages --- | --- | --- All ```<li>``` before ```<h2>``` "See Also" | [List of racehorses](https://en.wikipedia.org/wiki/List_of_racehorses)


| All tables: 1st column | [List of wars involving the Republic of China](https://en.wikipedia.org/wiki/List_of_wars_involving_the_Republic_of_China)<br>[List of James Bond films](https://en.wikipedia.org/wiki/List_of_James_Bond_films) |
| All ```<li>``` before ```<h2>``` "See Also", interspersed amongst non-relevant, hyperlinked ```<h2>``` and ```<h3>``` | [List of botanical gardens in the United Kingdom](https://en.wikipedia.org/wiki/List_of_botanical_gardens_in_the_United_Kingdom) |
| All tables: 1st column; all ```<li>``` before ```<h2>``` "See Also" | [List of islands of Scotland](https://en.wikipedia.org/wiki/List_of_islands_of_Scotland) |
| All tables: 1st column where heading = "[string that occurs in list title]" | [List of The Sopranos characters](https://en.wikipedia.org/wiki/List_of_The_Sopranos_characters) |
| All tables: 1st column with hyperlinks;<br>1st hyperlink inside all ```<li>``` before ```<h2>``` "See Also"<br>Most hyperlinked ```<h3>``` | [List of Chinese wars and battles](https://en.wikipedia.org/wiki/List_of_Chinese_wars_and_battles) |
| Unparseable | [List of Attack on Titan characters](https://en.wikipedia.org/wiki/List_of_Attack_on_Titan_characters)<br>[List of incidents of cannibalism](https://en.wikipedia.org/wiki/List_of_incidents_of_cannibalism)<br>[List of unusual units of measurement](https://en.wikipedia.org/wiki/List_of_unusual_units_of_measurement) |


Python scripts that pull data from Wikipedia
