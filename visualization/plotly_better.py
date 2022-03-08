# import plotly packages
import plotly.graph_objects as go
import plotly.express as px

## reading the data and looking at the 1st five rows using head()
df = px.data.gapminder()


# reading the datasets for India and China
df_india = df[df['country'] == 'India']
df_china = df[df['country'] == 'China']

## Using figure function to define the data argument and setting it to the bars for India and China
fig = go.Figure(data=[go.Bar(x=df_india['year'], y=df_india['pop'], marker_color = 'indianred',name = 'India'),
                        go.Bar(x=df_china['year'], y=df_china['pop'], marker_color = 'blue',name = 'China')
                        ])

## Setting the titles, xaxis and yaxis
fig.update_layout(title='Population of India and China over the years',
                  xaxis_title='Years',
                  yaxis_title='Population',
                  )

fig.show()

# step 1 : Setting the figure function
fig = go.Figure(data = [go.Scatter(x = df_india['year'], y = df_india['lifeExp'], \
                                   line = dict(color = 'firebrick', width = 4),
                                   text = df_india['country'], name = 'India'),
                        go.Scatter(x = df_china['year'], y = df_china['lifeExp'], \
                                   line = dict(color = 'blue', width = 4), text = df_china['country'], name = 'China')])


# step 2 : Setting the update_layout function
fig.update_layout(title='Life Expectency over the years',
                  xaxis_title='Years',
                  yaxis_title='Life Expectancy (years)',
                  )
fig.show()

fig = go.Figure(data = [go.Scatter(y = df_india['lifeExp'], x = df_india['gdpPercap'], \
                                   mode = 'markers', name = 'India')
    ,
                        go.Scatter(y = df_china['lifeExp'], x = df_china['gdpPercap'], \
                                   mode = 'markers', name = 'China')
                        ])


fig.update_layout(title='Life Expectency vs GDP per Capita',
                  yaxis_title='Life Expectancy (years)',
                  xaxis_title='gdpPercap',
                  )
fig.show()

df = px.data.gapminder()

fig = px.scatter(df, x = 'gdpPercap', y = 'lifeExp', size = 'pop',
                 color = 'continent', hover_name='country',
                 log_x= True, size_max=50, title = 'World Development in 2007',
                 animation_frame="year", animation_group="country", range_y = [25,90])

fig.update_layout(xaxis = dict(showgrid=False), yaxis = dict(showgrid=False))

fig.show()