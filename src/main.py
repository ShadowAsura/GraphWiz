import pygame
from ui.panels import SidePanel
from algorithms.bfs import bfs
from core.node import Node
from core.edge import Edge

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH, HEIGHT = 800, 600

side_panel = SidePanel(650, 0, 150, HEIGHT)

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

            # Check if click is on one of the side panel buttons
            for button in side_panel.buttons:
                if button.is_clicked(x, y) and button.text == "BFS":
                    # Convert nodes and edges to graph format for bfs
                    graph = {node: [] for node in nodes}
                    for edge in edges:
                        graph[edge.node1].append(edge.node2)
                        graph[edge.node2].append(edge.node1)

                    traversal_order = bfs(graph, nodes[0])

                    # Visualize the BFS traversal
                    for idx, node in enumerate(traversal_order):
                        # Highlight the current node in RED
                        node.color = (255, 0, 0)  # RED
                        screen.fill(WHITE)
                        for edge in edges:
                            edge.draw(screen)
                        for n in nodes:
                            n.draw(screen)
                        pygame.display.flip()

                        pygame.time.wait(100)  # Delay for visualization

                        # Mark the node as visited in GREEN
                        node.color = (0, 255, 0)  # GREEN
                        screen.fill(WHITE)
                        for edge in edges:
                            edge.draw(screen)
                        for n in nodes:
                            n.draw(screen)
                        pygame.display.flip()

                        pygame.time.wait(100)  # Delay for visualization

            # If the click wasn't on a button but was within the side panel, skip the rest
            if side_panel.is_clicked(x, y):
                continue

            clicked_nodes = [node for node in nodes if node.is_clicked(x, y)]

            if not clicked_nodes:  # If no node is clicked, create a new node
                nodes.append(Node(x, y))
            elif len(clicked_nodes) == 1:  # Initiate edge creation
                start_node = clicked_nodes[0]
                while pygame.mouse.get_pressed()[0]:  # Left button held down
                    screen.fill(WHITE)
                    
                    # Draw existing nodes and edges
                    for node in nodes:
                        node.draw(screen)
                    for edge in edges:
                        edge.draw(screen)
                    
                    end_x, end_y = pygame.mouse.get_pos()
                    pygame.draw.line(screen, (0, 0, 255), (start_node.x, start_node.y), (end_x, end_y))
                    pygame.display.flip()

                    for e in pygame.event.get():
                        if e.type == pygame.MOUSEBUTTONUP:
                            end_nodes = [node for node in nodes if node.is_clicked(end_x, end_y)]
                            if end_nodes:
                                end_node = end_nodes[0]
                                edges.append(Edge(start_node, end_node))

    # Draw nodes, edges, and side panel
    for node in nodes:
        node.draw(screen)
    for edge in edges:
        edge.draw(screen)
    side_panel.draw(screen)

    pygame.display.flip()

pygame.quit()

