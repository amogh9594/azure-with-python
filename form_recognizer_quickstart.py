# import libraries
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

context = {}
# set `<your-endpoint>` and `<your-key>` variables with the values from the Azure portal
endpoint = "xxxxxxxxxxxxxxx"
key = "xxxxxxxxxxxxxxxxxxxx"

def format_bounding_region(bounding_regions):
    if not bounding_regions:
        return "N/A"
    return ", ".join("Page #{}: {}".format(region.page_number, format_bounding_box(region.bounding_box)) for region in bounding_regions)

def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])


def analyze_general_documents():
    # sample document
    docUrl = "https://xxxxxxxxx/xxxxxxx/DATA SOFT.pdf"

    # create your `DocumentAnalysisClient` instance and `AzureKeyCredential` variable
    document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-document", docUrl)
    result = poller.result()

    '''
    for style in result.styles:
        if style.is_handwritten:
            print("Document contains handwritten content: ")
            print(",".join([result.content[span.offset:span.offset + span.length] for span in style.spans]))
    '''
    print("----Key-value pairs found in document----")
    for kv_pair in result.key_value_pairs:
        
        if kv_pair.key:
            '''
            print(
                    "Key '{}' ".format(
                        kv_pair.key.content,
                        format_bounding_region(kv_pair.key.bounding_regions),
                    )
                )
            ''' 
            Azure_key = kv_pair.key.content
            print("Data Type :", type(Azure_key))
            context["key"]=Azure_key
            print("----------------------------------------------------------------")
            print(context)

        if kv_pair.value:
            '''
            print(
                    "Value '{}' \n".format(
                        kv_pair.value.content,
                        format_bounding_region(kv_pair.value.bounding_regions),
                    )
                )
            '''
            Azure_value = kv_pair.value.content
            context["value"]=Azure_value
            print("----------------------------------------------------------------")    
            print(context)
    '''     
    print("----Entities found in document----")
    for entity in result.entities:
        print("Entity of category '{}' with sub-category '{}'".format(entity.category, entity.sub_category))
        print("...has content '{}'".format(entity.content))
        print("...within '{}' bounding regions".format(format_bounding_region(entity.bounding_regions)))
        print("...with confidence {}\n".format(entity.confidence))

    for page in result.pages:
        print("----Analyzing document from page #{}----".format(page.page_number))
        print(
            "Page has width: {} and height: {}, measured with unit: {}".format(
                page.width, page.height, page.unit
            )
        )

        for line_idx, line in enumerate(page.lines):
            print(
                "...Line # {} has text content '{}' within bounding box '{}'".format(
                    line_idx,
                    line.content,
                    format_bounding_box(line.bounding_box),
                )
            )

        for word in page.words:
            print(
                "...Word '{}' has a confidence of {}".format(
                    word.content, word.confidence
                )
            )

        for selection_mark in page.selection_marks:
            print(
                "...Selection mark is '{}' within bounding box '{}' and has a confidence of {}".format(
                    selection_mark.state,
                    format_bounding_box(selection_mark.bounding_box),
                    selection_mark.confidence,
                )
            )

    for table_idx, table in enumerate(result.tables):
        print(
            "Table # {} has {} rows and {} columns".format(
                table_idx, table.row_count, table.column_count
            )
        )
        for region in table.bounding_regions:
            print(
                "Table # {} location on page: {} is {}".format(
                    table_idx,
                    region.page_number,
                    format_bounding_box(region.bounding_box),
                )
            )
        for cell in table.cells:
            print(
                "...Cell[{}][{}] has content '{}'".format(
                    cell.row_index,
                    cell.column_index,
                    cell.content,
                )
            )
            for region in cell.bounding_regions:
                print(
                    "...content on page {} is within bounding box '{}'\n".format(
                        region.page_number,
                        format_bounding_box(region.bounding_box),
                    )
                )
    print("----------------------------------------")
    '''

if __name__ == "__main__":
    analyze_general_documents()
