import os
import re

def extract_bracket_content(folder_name):
    """Extract content inside brackets [] from the folder name."""
    match = re.search(r'\[(.*?)\]', folder_name)
    return match.group(1) if match else None

def find_similar_folders(base_folder):
    # List all folder names in the given base folder
    folder_names = [name for name in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, name))]
    similar_groups = []
    seen = set()

    # Compare all folder names based on their bracket content
    for i in range(len(folder_names)):
        folder1 = folder_names[i]
        content1 = extract_bracket_content(folder1)
        if content1 is None or content1 in seen:
            continue

        similar_group = [folder1]

        for j in range(i + 1, len(folder_names)):
            folder2 = folder_names[j]
            content2 = extract_bracket_content(folder2)

            if content1 == content2:
                similar_group.append(folder2)

        if len(similar_group) > 1:
            similar_groups.append(similar_group)
            seen.add(content1)

    return similar_groups

def save_to_txt(similar_groups, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for group in similar_groups:
            for folder in group:
                f.write(f"{folder}\n")
            f.write("These folders are similar\n\n")
    print(f"Similar folder names have been saved to {output_file}")

def main():
    # Automatically use the folder where the script/exe is located
    base_folder = os.getcwd()

    # Find similar folder names
    print(f"Scanning for similar folder names in: {base_folder}")
    similar_groups = find_similar_folders(base_folder)

    if similar_groups:
        # Save results to a .txt file
        output_file = os.path.join(base_folder, "similar_folders.txt")
        save_to_txt(similar_groups, output_file)
    else:
        print("No similar folder names found.")

if __name__ == "__main__":
    main()