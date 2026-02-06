#!/usr/bin/env python
"""
Setup script for Smart Mood-Based Music Suggestion System
Run this script to set up the Django project
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, description):
    """Run a shell command and report status"""
    print(f"\n{'='*60}")
    print(f"  {description}")
    print(f"{'='*60}")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✓ {description} - SUCCESS")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} - FAILED")
        print(f"Error: {e}")
        return False


def main():
    """Main setup function"""
    print("\n" + "="*60)
    print("  Smart Mood-Based Music Suggestion System Setup")
    print("="*60)
    
    # Get the project root directory
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    # Step 1: Create virtual environment
    print("\n[1/8] Creating virtual environment...")
    venv_path = project_root / 'venv'
    if not venv_path.exists():
        run_command(f'python -m venv venv', 'Creating virtual environment')
    else:
        print("  Virtual environment already exists")
    
    # Step 2: Activate virtual environment and install dependencies
    activate_cmd = 'venv\\Scripts\\activate.bat && ' if os.name == 'nt' else 'source venv/bin/activate && '
    
    print("\n[2/8] Installing dependencies...")
    run_command(f'{activate_cmd}pip install --upgrade pip', 'Upgrading pip')
    run_command(f'{activate_cmd}pip install -r requirements.txt', 'Installing dependencies')
    
    # Step 3: Create .env file
    print("\n[3/8] Setting up environment variables...")
    env_file = project_root / '.env'
    if not env_file.exists():
        print("  Creating .env file from .env.example")
        env_example = project_root / '.env.example'
        if env_example.exists():
            with open(env_example, 'r') as f:
                env_content = f.read()
            with open(env_file, 'w') as f:
                f.write(env_content)
            print("  ✓ .env file created")
    else:
        print("  .env file already exists")
    
    # Step 4: Create MySQL database
    print("\n[4/8] MySQL Database Setup Instructions")
    print("  Please run the following command in MySQL:")
    print("  mysql -u root -p -e \"CREATE DATABASE music_suggestion_db;\"")
    print("\n  Update your MySQL credentials in music_project/settings.py")
    
    # Step 5: Run migrations
    print("\n[5/8] Running Django migrations...")
    run_command(f'{activate_cmd}python manage.py makemigrations', 'Creating migrations')
    run_command(f'{activate_cmd}python manage.py migrate', 'Applying migrations')
    
    # Step 6: Collect static files
    print("\n[6/8] Collecting static files...")
    run_command(f'{activate_cmd}python manage.py collectstatic --noinput', 'Collecting static files')
    
    # Step 7: Create superuser
    print("\n[7/8] Creating superuser account...")
    print("  You will be prompted to create a superuser account")
    os.system(f'{activate_cmd}python manage.py createsuperuser')
    
    # Step 8: Setup instructions
    print("\n[8/8] Setup complete!")
    print("\n" + "="*60)
    print("  SETUP COMPLETE - Next Steps:")
    print("="*60)
    print("\n1. Update database credentials in music_project/settings.py")
    print("2. Add your YouTube API key to music_project/settings.py")
    print("3. Create the MySQL database:")
    print("   mysql -u root -p -e \"CREATE DATABASE music_suggestion_db;\"")
    print("\n4. To run the development server:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate.bat")
    else:
        print("   source venv/bin/activate")
    print("   python manage.py runserver")
    print("\n5. Visit http://localhost:8000 in your browser")
    print("\n6. Admin panel: http://localhost:8000/admin/")
    print("\n" + "="*60)


if __name__ == '__main__':
    main()
