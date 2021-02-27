import csv


class BaseballPlayer(object):

  def __init__(self, first_name, last_name, team_name, jersey_number):
    self.first_name = first_name
    self.last_name = last_name
    self.team_name = team_name
    self.jersey_number = jersey_number

  def __repr__(self):
    return (
      '{first_name: ' + self.first_name +
      ' last_name: ' + self.last_name +
      ' team: ' + self.team_name +
      ' number: ' + self.jersey_number + "}")
  
  def full_name(self):
    return self.first_name + ' ' + self.last_name



def read_baseball_players():
  '''
  Reads the data out of baseball.csv and returns a list of baseball player data
  '''
  baseball_players = []
  with open('Lesson_1/baseball_players.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)
    for row in csv_reader:
      baseball_players.append(
        BaseballPlayer(row[0], row[1], row[2], row[3]))
  return baseball_players

baseball_players = read_baseball_players();
