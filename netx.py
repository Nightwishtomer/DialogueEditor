import json
import networkx as nx
import matplotlib.pyplot as plt

# Загружаем твой JSON
with open("dialog.json", "r", encoding="utf-8") as f:
    data = json.load(f)

G = nx.DiGraph()

# добавляем узлы
for node in data["nodes"]:
    G.add_node(node["id"])

# добавляем связи (options -> next)
for node in data["nodes"]:
    if "options" in node:
        for option in node["options"]:
            nxt = option["next"]
            if isinstance(nxt, list):
                for n in nxt:
                    G.add_edge(node["id"], n, label=option["text"]["en"])
            else:
                G.add_edge(node["id"], nxt, label=option["text"]["en"])

# рисуем
pos = nx.spring_layout(G)  # можно заменить на nx.shell_layout, nx.planar_layout и т.п.

nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=8)
labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=7)

plt.show()
