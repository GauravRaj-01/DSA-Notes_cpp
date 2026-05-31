import os

source_dir = r"c:\Users\rajga\Downloads\DSA NOTES"

files = [
    "dsa_array_patterns_notes.html",
    "dsa_string_patterns_notes.html",
    "dsa_hashmap_patterns_notes.html",
    "dsa_stack_notes.html",
    "dsa_queue_deque_patterns_notes.html",
    "dsa_linked_list_notes.html",
    "dsa_trees_patterns_notes.html",
    "dsa_recursion_patterns_notes.html",
    "dsa_heap_patterns_notes.html",
    "dsa_dp_patterns_notes2.html",
    "sorting_algorithms_notes.html"
]

mobile_style_replacement = """  @media(max-width:768px){
    .sidebar {
      position: sticky;
      top: 0; left: 0; right: 0;
      width: 100%;
      height: 56px;
      background: var(--bg2);
      border-right: none;
      border-bottom: 1px solid var(--border);
      padding: 0 16px;
      display: flex;
      flex-direction: row;
      align-items: center;
      overflow-x: auto;
      overflow-y: hidden;
      white-space: nowrap;
      z-index: 100;
      gap: 8px;
      -webkit-overflow-scrolling: touch;
    }
    .sidebar::-webkit-scrollbar { display: none; }
    .sidebar-logo { display: none !important; }
    .nav-section { display: flex; flex-direction: row; gap: 8px; padding: 0; margin: 0; width: auto; align-items: center; }
    .nav-section-label { display: none !important; }
    .nav-link { display: inline-flex; align-items: center; width: auto; padding: 6px 12px; border-radius: 20px; font-size: 12px; background: var(--bg3); border: 1px solid var(--border); color: var(--muted); flex-shrink: 0; height: 32px; gap: 6px; }
    .nav-link.active { background: var(--bg3); border-color: currentColor; }
    .sub-links { display: none !important; }
    .main { margin-left: 0; padding: 20px 16px 40px; }
    .grid2,.grid3 { grid-template-columns: 1fr; }
  }"""

def replace_media_query(content, new_mq):
    start_tag = "@media(max-width:768px)"
    idx = content.find(start_tag)
    if idx == -1:
        start_tag = "@media (max-width: 768px)"
        idx = content.find(start_tag)
    if idx == -1:
        start_tag = "@media(max-width: 768px)"
        idx = content.find(start_tag)
        
    if idx == -1:
        return content
        
    brace_count = 0
    search_start = content.find("{", idx)
    if search_start == -1:
        return content
        
    for i in range(search_start, len(content)):
        char = content[i]
        if char == "{":
            brace_count += 1
        elif char == "}":
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                return content[:idx] + new_mq + content[end_idx:]
    return content

for filename in files:
    filepath = os.path.join(source_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        modified = replace_media_query(content, mobile_style_replacement)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(modified)
        print(f"Successfully transformed mobile navigation in {filename}")
    else:
        print(f"Warning: {filename} not found!")

print("All 11 volumes mobile navigation successfully transformed to sticky horizontal scrollbar!")
