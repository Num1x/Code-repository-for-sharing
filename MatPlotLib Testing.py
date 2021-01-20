import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0., 5., 0.2)
a = np.arange(1., 5., 0.2)

Team1Score = [1,2,3,4,5]
Team2Score = [1,4,6,8,10]
Team3Score = [1,8,12,16,20]
Team4Score = [1,16,24,32,40]
Team5Score = [1,32,48,64,80]
Team6Score = [1,64,96,128,160]
Team7Score = [1,1,1,1,1]
Team8Score = [1,1,1,1,1]
Team9Score = [1,1,1,1,1]
Team10Score = [1,1,1,1,1]
Team11Score = [1,1,1,1,1]
Team12Score = [1,1,1,1,1]

Team1linex = np.array([1,2,3,4,5])
Team1liney = np.array(Team1Score)

Team2linex = np.array([1,2,3,4,5])
Team2liney = np.array(Team2Score)

Team3linex = np.array([1,2,3,4,5])
Team3liney = np.array(Team3Score)

Team4linex = np.array([1,2,3,4,5])
Team4liney = np.array(Team4Score)
    
Team5linex = np.array([1,2,3,4,5])
Team5liney = np.array(Team5Score)

Team6linex = np.array([1,2,3,4,5])
Team6liney = np.array(Team6Score)

Team7linex = np.array([1,2,3,4,5])
Team7liney = np.array(Team7Score)

Team8linex = np.array([1,2,3,4,5])
Team8liney = np.array(Team8Score)

Team9linex = np.array([1,2,3,4,5])
Team9liney = np.array(Team9Score)

Team10linex = np.array([1,2,3,4,5])
Team10liney = np.array(Team10Score)

Team11linex = np.array([1,2,3,4,5])
Team11liney = np.array(Team11Score)

Team12linex = np.array([1,2,3,4,5])
Team12liney = np.array(Team12Score)

team1Color = '#FF0000'
team2Color = '#2B00FF'
team3Color = '#00C4FF'
team4Color = '#00FF3C'
team5Color = '#FFAB00'
team6Color = '#003300'
team7Color = 0
team8Color = 0 
team9Color = 0
team10Color = 0
team11Color = 0 
team12Color = 0



plt.plot(Team1linex, Team1liney, team1Color, Team2linex, Team2liney, team2Color, Team3linex, Team3liney, team3Color, Team4linex, Team4liney, team4Color, Team5linex, Team5liney, team5Color, Team6linex, Team6liney, team6Color)




plt.title('Team Scores')
plt.ylabel('Points scored')
plt.xlabel('Match Number')
plt.axis([1,5,0,500])
plt.show()
