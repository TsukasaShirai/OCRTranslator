import ui, console
import translator
import ocr
import photos
import io

def displayConvertedData(sender):

	pil_img=photos.capture_image()

	if pil_img is None:
		return
	
	size = (int(pil_img.size[0]*0.3), int(pil_img.size[1]*0.3))
	pil_img = pil_img.resize(size)
	
	img = io.BytesIO()
	pil_img.save(img,"JPEG")
	img_byte = img.getvalue()
	doc = ocr.getDoc(img_byte)
	lines = doc.split('.')

	textview = sender.superview['textview']
	for line in lines:
		if line is not None:
			textview.text += '\n\n' + line + "."
			textview.text += '\n\n*' + translator.translate(line + ".")

def renewText(sender):
	if console.alert('クリア','テキストをクリアしますか？','OK') == 1:
		textview = sender.superview['textview']
		textview.text = ''
	
v = ui.load_view()
v.present('sheet')
