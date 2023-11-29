import altair as alt

#Plots chart of victims
def victim_chart(victim):
    chart = alt.Chart(victim, title = "Age and Gender of Victims 2020 - 2023").mark_bar().encode(
    alt.X("Vict Age:Q", 
    title='Victim Age (Bin 5)' ,
    bin = alt.Bin(maxbins=20)),
    y="count()",
    color = alt.Color("Vict Sex", title="Gender",  scale=alt.Scale(range=['orange','lightyellow']))  
    )
    return chart