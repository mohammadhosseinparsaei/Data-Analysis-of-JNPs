import matplotlib.pyplot as plt

def pairwise_comparison(num1, num2, p_adj, center, height, yerr=None, dh=.05, barh=.05, fs=None, bold=False, maxasterix=None, line_width=None, vertical=False):
    if isinstance(p_adj, str):
        text = p_adj
    else:
        if p_adj < 0.0001:
            text = '****'
        elif p_adj < 0.001:
            text = '***'
        elif p_adj < 0.01:
            text = '**'
        elif p_adj < 0.05:
            text = '*'
        else:
            text = 'ns'

    lx, ly = center[num1], height[num1]
    rx, ry = center[num2], height[num2]

    if not vertical:
        if yerr:
            ly += yerr[num1]
            ry += yerr[num2]
        ax_y0, ax_y1 = plt.gca().get_ylim()
        dh *= (ax_y1 - ax_y0)
        barh *= (ax_y1 - ax_y0)
        y = max(ly, ry) + dh
        barx = [lx, lx, rx, rx]
        bary = [y, y+barh, y+barh, y]
        mid = ((lx+rx)/2, y+barh)
        kwargs = dict(ha='center', va='bottom')
    else:
        ay_x0, ay_x1 = plt.gca().get_xlim()
        dh *= (ay_x1 - ay_x0)
        barh *= (ay_x1 - ay_x0)
        x = max(lx, rx) + dh
        barx = [x, x+barh, x+barh, x]
        bary = [ly, ly, ry, ry]
        mid = (x+barh, (ly+ry)/2)
        kwargs = dict(ha='left', va='center')

    if line_width is not None:
        plt.plot(barx, bary, c='black', linewidth=line_width)
    else:
        plt.plot(barx, bary, c='black')

    if fs is not None:
        kwargs['fontsize'] = fs
    if bold:
        kwargs['fontweight'] = 'bold'

    plt.text(*mid, text, **kwargs)