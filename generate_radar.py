import matplotlib.pyplot as plt
import numpy as np

# Labels & data (replace with your actual stats if needed)
labels = ["Code Review", "Issues", "Pull Requests", "Commits"]
data = [26, 15, 3, 56]  # Your real numbers here
data += data[:1]  # Close the loop

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))

# Radar chart
ax.plot(angles, data, color="#30d158", linewidth=2)
ax.fill(angles, data, color="#30d158", alpha=0.25)

# Labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticklabels([])

# Save as SVG
plt.savefig("github_radar_chart.svg", format="svg", bbox_inches='tight')
print("Radar chart generated successfully!")
