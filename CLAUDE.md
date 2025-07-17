# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based CV image optimization tool that processes profile images and integrates them into PDF documents. The tool creates circular profile images and inserts them into both Green and Orange themed CV templates, with final PDF compression for professional use.

## Key Commands

### Development & Execution
```bash
# Main workflow execution
python main.py                    # Run complete CV optimization workflow
uv run python main.py            # Run with uv package manager

# Module testing (standalone execution)
python src/crop_circle.py         # Test image cropping functionality
python src/insert_image.py        # Test PDF image insertion
python src/compress_pdf.py        # Test PDF compression
python test_compression.py        # Compare all compression methods
```

### Package Management
```bash
# Install/update dependencies
uv sync                          # Install dependencies from uv.lock
uv add package-name              # Add new dependency
uv remove package-name           # Remove dependency
```

### System Dependencies
```bash
# Install Ghostscript (required for PDF compression)
brew install ghostscript         # macOS
sudo apt-get install ghostscript # Ubuntu/Debian
```

## Architecture & Structure

### Core Processing Pipeline
The application follows a **3-stage pipeline architecture**:

1. **Image Processing** (`src/crop_circle.py`):
   - Crops rectangular images to perfect squares
   - Applies circular mask with transparency
   - Configurable positioning and padding controls

2. **PDF Integration** (`src/insert_image.py`):
   - Uses PyMuPDF (fitz) for PDF manipulation
   - Inserts circular images at precise coordinates
   - Processes both Green and Orange CV variants

3. **PDF Compression** (`src/compress_pdf.py`):
   - Multiple compression algorithms via Ghostscript
   - Quality optimization with 7 different strategies
   - File size analysis and reporting

### Key Modules

#### `src/main_workflow.py`
- **Purpose**: Orchestrates the complete workflow
- **Key Features**: Input validation, error handling, progress tracking
- **Workflow**: Single image → two themed PDFs → compressed outputs

#### `src/crop_circle.py`
- **Purpose**: Converts rectangular images to circular profile pictures
- **Key Parameters**:
  - `vertical_shift_pct=0.05`: Optimized for face positioning
  - `horizontal_shift_px=16`: Fine-tuned horizontal alignment
  - `padding_pct=0.06`: Circle size relative to image bounds

#### `src/insert_image.py`
- **Purpose**: Embeds circular images into PDF documents
- **Key Parameters**:
  - `position=(35, 22)`: Optimized coordinate placement
  - `size=(110, 110)`: Professional CV image size (points)

#### `src/compress_pdf.py`
- **Purpose**: Optimizes PDF file sizes while maintaining quality
- **Key Features**:
  - 7 compression strategies: screen, ebook, printer, prepress, custom variants
  - Default: "custom-balanced" for optimal CV quality
  - Ghostscript integration with extensive parameter control

## File Structure & Data Flow

### Input Files
```
data/
├── images/
│   ├── cv-image.jpg          # Primary profile image
│   └── cv-image-2.jpg        # Alternative image
└── pdfs/
    ├── cv.pdf       # Green themed CV template
    └── cv (1).pdf   # Orange themed CV template
```

### Output Files (Sequential Numbering)
```
output/
├── 01-crop-circle-output.png           # Circular profile image
├── cv-with-image.pdf                   # Green CV with image
├── 02-cv (1)-with-image.pdf            # Orange CV with image
├── cv-robin-walter-scherler-gr.pdf     # Compressed Green CV
└── cv-robin-walter-scherler-or.pdf     # Compressed Orange CV
```

## Development Workflow

### Adding New Features
1. **Image Processing**: Modify `src/crop_circle.py` for new cropping features
2. **PDF Integration**: Extend `src/insert_image.py` for positioning/styling
3. **Compression**: Add new strategies to `src/compress_pdf.py`
4. **Workflow**: Update `src/main_workflow.py` for new processing steps

### Testing Approach
- **Integration Testing**: Use `python main.py` for end-to-end testing
- **Module Testing**: Execute individual source files for component testing
- **Compression Testing**: Use `python test_compression.py` for quality comparison
- **Manual Verification**: Visual inspection of generated PDFs

### Error Handling
- Comprehensive input validation in `main_workflow.py`
- Missing file detection with detailed error messages
- Exception handling with German user feedback
- File size analysis and compression ratio reporting

## Key Configuration Parameters

### Optimized Settings (Pre-configured)
```python
# Image cropping (crop_circle.py)
vertical_shift_pct=0.05      # Face positioning optimization
horizontal_shift_px=16       # Horizontal alignment
padding_pct=0.06            # Circle size control

# PDF positioning (insert_image.py)  
position=(35, 22)           # Precise coordinate placement
size=(110, 110)            # Professional CV image size

# Compression (compress_pdf.py)
quality="custom-balanced"   # Optimized for CV documents
```

### Compression Quality Options
- `screen`: Web optimization, smallest files
- `ebook`: Balanced for digital reading
- `printer`: Standard print quality
- `prepress`: High-quality printing
- `custom-balanced`: **Default** - CV-optimized quality/size ratio
- `custom-high`: Maximum quality retention
- `custom-small`: Aggressive compression

## Dependencies & Requirements

### Python Dependencies
```toml
pillow>=11.3.0              # Image processing and manipulation
pymupdf>=1.26.3             # PDF reading, editing, and creation
```

### System Requirements
- Python 3.10 or higher
- Ghostscript (for PDF compression)
- uv package manager (recommended)

### External Tools
- **Ghostscript**: Required for PDF compression functionality
- **uv**: Modern Python package manager for dependency management

## Important Notes

### Language & Localization
- User interface messages are in German
- File paths and internal code use English
- Error messages and progress indicators use German terminology

### Quality Optimization
- Parameters are pre-tuned for professional CV image quality
- Multiple compression strategies ensure optimal file size vs. quality balance
- Skin tone preservation in image processing pipeline

### File Management
- Sequential numbering system (01-, 02-, 03-) for clear workflow tracking
- Automatic output directory creation
- Non-destructive processing (original files preserved)

### Performance Considerations
- Single circular image reused for both PDF variants
- Efficient memory usage with PIL optimizations
- Ghostscript subprocess management for compression