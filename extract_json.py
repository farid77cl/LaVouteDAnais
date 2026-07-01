import json
import sys

def main():
    try:
        with open(r'C:\Users\farid\.gemini\antigravity\brain\bec1acab-2921-42e5-b92e-ea0427f9f99b\scratch\prompts_extraidos.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        looks = ['246', '247']
        poses = ['back_view', 'seated', 'side_profile', 'pov', 'odalisque']
        
        result = {}
        for look in looks:
            if look in data:
                result[look] = {}
                for pose in poses:
                    result[look][pose] = data[look].get('prompts', {}).get(pose, '')
        
        with open('C:/Users/farid/LaVouteDAnais/extracted_prompts.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
            
        print("Success. Wrote to C:/Users/farid/LaVouteDAnais/extracted_prompts.json")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
