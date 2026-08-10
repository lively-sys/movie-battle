#Defining classes for movie and movie lineup

from functools import total_ordering

#Create Movie class with the ability to compare instances
@total_ordering
class Movie:
    def __init__(self, title, primary_data, secondary_data, tertiary_data):
        self.title = title
        self.primary_data = primary_data
        self.secondary_data = secondary_data
        self.tertiary_data = tertiary_data
    
    def __eq__(self, other):
        return self.primary_data == other.primary_data and self.secondary_data == other.secondary_data and self.tertiary_data == other.tertiary_data

    def __lt__(self, other):
        return (self.primary_data < other.primary_data or
                (self.primary_data == other.primary_data and self.secondary_data < other.secondary_data) or
                (self.primary_data == other.primary_data and self.secondary_data == other.secondary_data and self.tertiary_data < other.tertiary_data))

#Create GroupLineup class to hold a lineup of movies with their primary data
class GroupLineup:
    def __init__(self, score: Movie, revenue: Movie, runtime: Movie, release_date: Movie):
        self.score = score
        self.revenue = revenue
        self.runtime = runtime
        self.release_date = release_date