# Living People - given a list of people, their year of birth and year of death compute the
# year with the most number of people alive. Count the year that people were born adn died as
# alive. Peter Koppelman January 18, 2018

import matplotlib.pyplot as plt


def living_people():
    people_dict = {1: [1930, 1993], 2: [1940, 2005], 3: [1941, 2010], 4: [1939, 2015],
                   5: [1940, 2011], 6: [1937, 2009], 7: [1939, 2013]}
    people_years = {}

    def populate_dict():
        # For each key, value pair in the dictionary.
        for x in range(1, len(people_dict) + 1):
            # Loop through each year from birth to death (inclusive)
            for year in range(people_dict[x][0], people_dict[x][1] + 1):
                # if year already in people_years increment the value by 1
                # else add a new key, value pair with the year and 1.
                if year in people_years:
                    people_years[year] += 1
                else:
                    people_years.update({year: 1})

    def graph():
        plt.plot(list(people_years.keys()), list(people_years.values()))
        plt.xlabel('Year')
        plt.ylabel('No. of People Alive')
        plt.title('No. of People Alive Each Year')
        plt.show()

    populate_dict()
    graph()


if __name__ == '__main__':
    living_people()
