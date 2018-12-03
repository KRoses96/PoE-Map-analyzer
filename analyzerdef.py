def chaosgp(self):
    df.plot.line(y= 'Chaos')
    df.plot.box(y='Chaos')
    plt.title('Chaos')
    plt.show()
def chaostat(self):
    grp = df.groupby(to_grp,squeeze = True)['Chaos'].agg(['min', 'mean', 'max'])
    print(grp.head())
    print('Total:')
    print(valc)
def cardgp(self):
    c1=df.plot(y = 'Card')
    c2=df.plot.box(y='Card')
    plt.show()
def cardstat(self):
    grp = df.groupby(to_grp)['Card'].agg(['min', 'mean', 'max'])
    print('Total:')
    print(valcdr)
    print(grp.head())
def exaltgp(self):
    df.plot(y = 'Exalt')
    df.plot.box(y='Exalt')
    plt.show()

def exaltstat(self):
    grp = df.groupby(to_grp)['Exalt'].agg(['min', 'mean', 'max'])
    print(grp.head())
    print('Total:')
    print(vale)

def fusegp(self):
    df.plot(y = 'Fuses')
    df.plot.box(y='Fuses')
    plt.show()
def fusestat(self):
    grp = df.groupby(to_grp)['Fuses'].agg(['min', 'mean', 'max'])
    print('Total:')
    print(valf)

def jewgp(self):
        df.plot(y = 'Jews')
        df.plot.box(y='Jews')
        plt.show()
def jewstat(self):
        grp = df.groupby(to_grp)['Jews'].agg(['min', 'mean', 'max'])
        print(grp.head())
        print('Total:')
        print(valj)

def returngp(self):
        df.plot(y = 'Returns')
        df.plot.box(y='Returns')
        plt.show()
def returnstat(self):
        grp = df.groupby(to_grp)['Returns'].agg(['min', 'mean', 'max'])
        print(grp.head())
        print('Total:')
        print(valret)

def miscgp(self):
    df.plot(y = 'Misc')
    plt.show()
def miscstat(self):
    grp = df.groupby(to_grp)['Misc'].agg(['min', 'mean', 'max'])
    print(grp.head())
    print('Total Chaos Worth Of Misc Drops:')
    print(valm)
def supersum(self):
    print(supersum)
