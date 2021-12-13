import graphviz

dot = graphviz.Digraph(comment='Game Algorithm')

dot.node('A', 'Robot')
dot.node('B', 'Defending')
dot.node('C', 'Attacking')
dot.node('D', 'Defensive')
dot.node('E', ' Offensive')

dot.edges(['AB','AC','CE','BD'])

doctest_mark_exe()
dot.render('test.gv',view=True)
