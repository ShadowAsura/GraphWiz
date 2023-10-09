import pygame

from ui.panels import SidePanel
from ui.buttons import Button

from algorithms.bfs import bfs
from algorithms.dfs import dfs

from core.node import Node
from core.edge import Edge

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH, HEIGHT = 800, 600

side_panel = SidePanel(650, 0, 150, HEIGHT)

clear_button = Button(660, 350, 130, 40, text="Clear", color=(214, 56, 56), font_color=(255, 255, 255))

side_panel.buttons.append(clear_button)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GraphWiz')

nodes = []
edges = []

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # Check if the click is on one of the side panel buttons
            for button in side_panel.buttons:
                if button.is_clicked(x, y):
                    if button.text == "BFS":
                        if not nodes:
                            print("Please create some nodes before running BFS.")
                            continue

                        graph = {node: [] for node in nodes}
                        for edge in edges:
                            graph[edge.node1].append(edge.node2)
                            graph[edge.node2].append(edge.node1)

                        traversal_order = bfs(graph, nodes[0])
                        
                        for node in traversal_order:
                            node.color = (0, 255, 0)  # GREEN
                            screen.fill(WHITE)

                            # Draw nodes, edges, and side panel
                            for edge in edges:
                                edge.draw(screen)
                            for n in nodes:
                                n.draw(screen)
                            side_panel.draw(screen)
                            
                            pygame.display.flip()
                            pygame.time.wait(500)  # 500ms delay for visualization
                        
                        for node in nodes:
                            node.color = (0, 0, 255)  # Reset to BLUE

                    if button.text == "DFS":
                        if not nodes:
                            print("Please create some nodes before running DFS.")
                            continue

                        graph = {node: [] for node in nodes}
                        for edge in edges:
                            graph[edge.node1].append(edge.node2)
                            graph[edge.node2].append(edge.node1)

                        traversal_order = dfs(graph, nodes[0])
                        
                        for node in traversal_order:
                            node.color = (255, 0, 0)  # RED
                            screen.fill(WHITE)

                            # Draw nodes, edges, and side panel
                            for edge in edges:
                                edge.draw(screen)
                            for n in nodes:
                                n.draw(screen)
                            side_panel.draw(screen)
                            
                            pygame.display.flip()
                            pygame.time.wait(100)  # 100ms delay for visualization
                        
                        for node in nodes:
                            node.color = (0, 0, 255)  # Reset to BLUE

                    if button.text == "Clear":
                        nodes = []
                        edges = []

            # Check if the click wasn't on a button but was within the side panel
            if side_panel.is_clicked(x, y):
                continue

            # Node and edge removal logic with shift key held down
            if pygame.key.get_pressed()[pygame.K_LSHIFT]:
                clicked_nodes = [node for node in nodes if node.is_clicked(x, y)]
                if clicked_nodes:
                    node_to_remove = clicked_nodes[0]
                    edges = [edge for edge in edges if edge.node1 != node_to_remove and edge.node2 != node_to_remove]
                    nodes.remove(node_to_remove)
                continue

            # Node and edge creation logic
            clicked_nodes = [node for node in nodes if node.is_clicked(x, y)]
            if not clicked_nodes:
                nodes.append(Node(x, y))
            elif len(clicked_nodes) == 1:
                start_node = clicked_nodes[0]
                
                drawing_edge = True
                while drawing_edge:
                    for e in pygame.event.get():
                        if e.type == pygame.MOUSEMOTION:
                            end_x, end_y = pygame.mouse.get_pos()
                            screen.fill(WHITE)

                            # Draw nodes, edges, and side panel
                            for edge in edges:
                                edge.draw(screen)
                            for node in nodes:
                                node.draw(screen)
                            side_panel.draw(screen)

                            pygame.draw.line(screen, (0, 0, 255), (start_node.x, start_node.y), (end_x, end_y))
                            pygame.display.flip()
                            
                        if e.type == pygame.MOUSEBUTTONUP:
                            end_x, end_y = pygame.mouse.get_pos()
                            end_nodes = [node for node in nodes if node.is_clicked(end_x, end_y)]
                            if end_nodes:
                                end_node = end_nodes[0]
                                edges.append(Edge(start_node, end_node))
                            drawing_edge = False

    # Drawing nodes, edges, and side panel outside the event loop
    for edge in edges:
        edge.draw(screen)
    for node in nodes:
        node.draw(screen)
    side_panel.draw(screen)

    pygame.display.flip()

pygame.quit()

