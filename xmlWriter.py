import glob
import xml.dom.minidom
import cv2





# def write_xml(filename):
if __name__ == "__main__":
    #1. 创建dom树对象
    xmlFilePath = glob.glob(r'xml/*')
    imgPath = glob.glob(r'result/*')
    imgcounter = 0
    # print(xmlFilePath[0][4:-4])
    for _ in xmlFilePath:
        dom = xml.dom.minidom.parse(_)

        doc = xml.dom.minidom.Document()
        #2. 创建根结点，并用dom对象添加根结点
        root_node = doc.createElement("annotation")
        doc.appendChild(root_node)

        #3. 创建结点，结点包含一个文本结点, 再将结点加入到根结点
        folder_node = doc.createElement("folder")
        folder_value = doc.createTextNode('NA')
        folder_node.appendChild(folder_value)
        root_node.appendChild(folder_node)

        filename_node = doc.createElement("filename")
        filename_value = doc.createTextNode(imgPath[imgcounter][7:])

        filename_node.appendChild(filename_value)
        root_node.appendChild(filename_node)

        source_node = doc.createElement("source")
        database_node = doc.createElement("database")
        database_node.appendChild(doc.createTextNode("Unknown"))
        source_node.appendChild(database_node)
        root_node.appendChild(source_node)

        size_node = doc.createElement("size")
        for item, value in zip(["width", "height", "depth"], [1280, 720, 3]):
            elem = doc.createElement(item)
            elem.appendChild(doc.createTextNode(str(value)))
            size_node.appendChild(elem)
        root_node.appendChild(size_node)

        seg_node = doc.createElement("segmented")
        seg_node.appendChild(doc.createTextNode(str(0)))
        root_node.appendChild(seg_node)

        root = dom.documentElement
        name = root.getElementsByTagName('name')
        xmin = root.getElementsByTagName('LeftX')
        ymin = root.getElementsByTagName('LeftY')
        xmax = root.getElementsByTagName('RightX')
        ymax = root.getElementsByTagName('LeftY')
        for i in range(name.length):
            obj_node = doc.createElement("object")
            name_node = doc.createElement("name")
            name_node.appendChild(doc.createTextNode(name[i].firstChild.data))
            obj_node.appendChild(name_node)

            pose_node = doc.createElement("pose")
            pose_node.appendChild(doc.createTextNode("Unspecified"))
            obj_node.appendChild(pose_node)

            trun_node = doc.createElement("truncated")
            trun_node.appendChild(doc.createTextNode(str(0)))
            obj_node.appendChild(trun_node)

            trun_node = doc.createElement("difficult")
            trun_node.appendChild(doc.createTextNode(str(0)))
            obj_node.appendChild(trun_node)

            trun_node = doc.createElement("occluded")
            trun_node.appendChild(doc.createTextNode(str(0)))
            obj_node.appendChild(trun_node)
            bndbox_node = doc.createElement("bndbox")
            for item, value in zip(["xmin", "ymin", "xmax", "ymax"], [xmin[i].firstChild.data, ymin[i].firstChild.data, xmax[i].firstChild.data, ymax[i].firstChild.data]):
                elem = doc.createElement(item)
                elem.appendChild(doc.createTextNode(str(value)))
                bndbox_node.appendChild(elem)
            obj_node.appendChild(bndbox_node)
            root_node.appendChild(obj_node)


        with open('xmlfinal/' + imgPath[imgcounter][7:-3] + 'xml', "w", encoding="utf-8") as f:
            # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
            # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
            doc.writexml(f, indent='', addindent='\t', newl='\n', encoding="utf-8")

        # 每一个结点对象（包括dom对象本身）都有输出XML内容的方法，如：toxml()--字符串, toprettyxml()--美化树形格式。
        # print(doc.toxml(encoding="utf-8"))  # 输出字符串
        # print(doc.toprettyxml(indent='', addindent='\t', newl='\n', encoding="utf-8"))   #输出带格式的字符串
        # doc.writexml() #将prettyxml字符串写入文件
        imgcounter = imgcounter + 1
    finalxmlpath = glob.glob(r'xmlfinal/*')
    for _ in finalxmlpath:
        with open(_, 'r') as r:
            lines = r.readlines()
        with open(_, 'w') as w:
            for l in lines:
                if '<?xml version="1.0" encoding="utf-8"?>' in l:
                    w.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
                    w.write('\n')
                else:
                    w.write(l)
