def plot_a():
    import matplotlib.pyplot as plt
    import seaborn as sns
    penguins = sns.load_dataset("penguins")

    sns.set_style('whitegrid',  rc = {'axes.grid' : True, 'axes.edgecolor': '0'}  )

    sns.set_context('paper', font_scale=2)



    # Create a visualization
    fig1 = sns.relplot(
        data=penguins,
        x="bill_length_mm", y="bill_depth_mm",
        hue="species", style="species",
        palette=[ [0.8,0.8,0.8],  [0,0,0], [0.6,0.6,0.6],],
        legend = True,  s=40, edgecolor= "k", alpha = 0.8
    )

    fig1.set_xlabels("Bill length in mm")
    fig1.set_ylabels("Bill depth in mm")


    plt.show()

    fig1.savefig("plot_a--huber_j.png") 

def plot_b():
    import matplotlib.pyplot as plt
    import seaborn as sns
    penguins = sns.load_dataset("penguins")

    sns.set_theme(style="whitegrid", rc = {'axes.grid' : False})


    sns.set_style('ticks', {'axes.edgecolor': '0',  
                            'xtick.color': '0',
                            'xtick.color': '0'}
                )

    penguins = sns.load_dataset("penguins")

    # Draw a nested barplot by species and sex
    fig2 = sns.catplot(
        data=penguins, kind="bar",
        x="species", y="body_mass_g", hue="sex",
        ci= False, palette=[[230/255,128/255,41/255], [0,65/255,110/255]],
        aspect = 1.618, legend = False, saturation = 1
    )

    #g.despine(left=True)
    fig2.set(ylim = (3000,5000))

    fig2.despine(offset=10, trim=True)
    fig2.set_axis_labels("", "Body mass in g")

    fig2.savefig("plot_b--huber_j.png", dpi = 400) 