from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name


class LoginPageLocators(object):
    input_username = (By.ID, "ctl00_ctl00_Main_BoxContent_txtUserName")
    input_password = (By.ID, "ctl00_ctl00_Main_BoxContent_txtPassword")
    login_button = (By.ID, "ctl00_ctl00_Main_BoxContent_BtnAuthenticate")


# all the xpath should be redefined according client requirement

class WelcomePageLocators(object):
    AdminLocator = (By.CLASS_NAME, "primaryMenuItemSel")
    CompaniesAndContactsLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[1]")
    IPAndProductsLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[2]")
    ParticipationManagerLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[3]")
    ReceivablesLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[4]")
    ContractApprovalsLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[5]")
    ApprovalWorkflowLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[6]")
    ContentLibraryLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[7]")


class CompaniesAndContactPageLocators(object):
    addNewCompanyLocator = (By.ID, "ctl00_ActionsContent_idAddNewLink")
    
    # Company Info
    CompanyName = (By.ID, "txtCompanyName")
    AboutTextBox = (By.ID, "txtAbout")
    companyCode = (By.ID, "txtAbbrev")
    ParentCompany = (By.ID, "ddlParentComp")
    owned = (By.ID, "cbOwned")
    TaxID = (By.ID, "txtTaxId")
    TaxID2 = (By.ID, "txtTaxId2")
    companyStatus = (By.ID, "ddlCompanyStatus")
    BusinessCategory = (By.ID, "msBusinesCategory_hrefOnItemsList")
    SearchBusinessCategory = (By.ID, "msBusinesCategory_txtSearch")
    # BusinessCategoryCheckBox = (By.ID, "checkbox_msBusinesCategory_gridItems_Incl_1")
    BusinessCategoryCheckBox = (By.XPATH, '//*[@id="msBusinesCategory_gridItems_top_head"]/td[1]/div/input')
    BusinessCategoryDone = (By.ID, "msBusinesCategory_btnDone")

    addLink = (By.ID, "msBusinesCategory_hrefOnItemsList")
    phoneNum = (By.ID, "txtPhone")
    faxNum = (By.ID, "txtFax")
    emailAddress = (By.ID, "txtEmailId")
    website = (By.ID, "txtWebsite")
    doingBusinessAs = (By.ID, "txtDoingBusinessAs")

    # Company User's Part
    canEditUsersCheckbox = (By.ID, "cbCanUsersEditData")
    SelectAddress = (By.ID, "ddlExistingAddressForDisplay")

    # Address
    AddressField1 = (By.ID, "txtAddress1")
    AddressField2 = (By.ID, "txtAddress2")
    cityInput = (By.ID, "txtCity")
    CountrySelect = (By.ID, "ddlCountry")
    StateSelect = (By.ID, "ddlState")
    zipCode = (By.ID, "txtPostCode")


    # Save / Cancel
    saveButton = (By.ID, "btnSave")
    cancelButton = (By.ID, "btnCancel")
    uploadButton = (By.ID, "btnUpload")

class IPandProductsPageLocators(object):
    productsMenuLocator = (By.ID, "wsSecondaryMenuItem_302")

    addNewIP = (By.ID, "ctl00_ActionsContent_idAddNewLink")
    addNewProduct = (By.ID, "ctl00_ContentPlaceHolder1_idAddNewLink")

    #Intellectual Proerty Details
    Addlicensor = (By.ID, "msLicensor_hrefOnItemsList")
    searchLicensor = (By.ID, "msLicensor_txtSearch")
    checkLicensor = (By.XPATH, "/html/body/form/div[4]/div[1]/div/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/div[2]/div[2]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[1]/div/input")
    LicensorCheckDone = (By.ID, "msLicensor_btnDone")

    intellectualProperty = (By.ID, "txtIPName")
    primaryID = (By.ID, "txtPrimaryID")
    owner = (By.ID, "IPStringSelector0_ListItem_search")
    property = (By.ID, "IPStringSelector1_ListItem_search")
    collection = (By.ID, "IPStringSelector2_ListItem_search")
    EAN = (By.ID, "IPStringSelector3_ListItem_search")

    addIPType = (By.ID, "msIPType_hrefOnItemsList")
    searchIPType = (By.ID, "msIPType_txtSearch")
    # checkIPType = (By.ID, "checkbox_msIPType_gridItems_Incl_1")
    checkIPType = (By.XPATH, '//*[@id="msIPType_gridItems_top_head"]/td[1]/div/input')
    checkIPTypeDone = (By.ID, "msIPType_btnDone")

    Language = (By.ID, "ddlLanguage")
    Status = (By.ID, "ddlStatus")
    Created = (By.ID, "dtCreated_txtDate")
    released = (By.ID, "dtReleased_txtDate")
    GLAcntCode = (By.ID, "txtGLAccountCode")
    accuralRate = (By.ID, "txtAccrualRate")
    Notes = (By.ID, "txtNote")

    #save/cancel
    saveButton2 = (By.ID, "btnSaveCheck")
    cancelButton2 = (By.ID, "btnCancel")

class ContactsLocator(object):
    addContactsLocator = (By.XPATH, '/html/body/form/div[3]/div/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td[10]/div/a[2]')
    situation = (By.ID, "ddlSalutation")
    firstName = (By.ID, "txtFirstName")
    MiddleName = (By.ID, "txtMiddleName")
    LastName = (By.ID, "txtLastName")
    JobTitle = (By.ID, "txtJobTitle")
    DisplayName = (By.ID, "txtDisplayName")
    referenceCode = (By.ID, "txtReferenceCode")
    email = (By.ID, "txtEmail")
    website = (By.ID, "txtWebsite")
    IMAddress = (By.ID, "txtIMAddress")

    #Phones
    businessPhone = (By.ID, "txtPhoneBus")
    homePhone = (By.ID, "txtPhoneHome")
    mobilePhone = (By.ID, "txtPhoneCell")
    businessFax = (By.ID, "txtBusinessFax")

    #Roles
    addRoles = (By.ID, "msRoles_hrefOnItemsList")
    searchRole = (By.ID, "msRoles_txtSearch")
    checkRole = (By.XPATH, "/html/body/form/div[4]/div/div[1]/table/tbody/tr/td[1]/table[4]/tbody/tr[2]/td[1]/div[2]/div[2]/table/tbody/tr/td/table/tbody/tr[1]/td[1]/div/input")
    checkRoleDone = (By.ID, "msRoles_btnDone")

    #image upload
    addPhoto = (By.ID, "aAddPhoto")
    fileUpload = (By.ID, "FileUpload1")
    buttonUplaod = (By.ID, "btnUpload")


    #save/cancel
    saveBtn3 = (By.ID, "btnSave")
    cancelBtn3 = (By.ID, "btnCancel")

class AddProductsLocatord(object):
    productCategoryLocator = (By.XPATH, '//*[@id="ctl00_caLeftMenu_1"]/nobr')
    productSubCategoryLocator = (By.XPATH, '//*[@id="ctl00_caLeftMenu_2"]/nobr')
    productArticlesLocator = (By.XPATH, '//*[@id="ctl00_caLeftMenu_3"]/nobr')

    frameLocator = (By.ID, "ctl00_ContentPlaceHolder1_WndHostctrl1_ifrm")
    productNameLocator = (By.ID, "txtProductName")
    primaryNumber = (By.ID, "txtPrimaryNumber")
    addNewLocator = (By.ID, "ctl00_MainContent_DefaultsCtrl1_idAddNewLink")
    categoryName = (By.ID, "")
    categoryDescription = (By.ID, "txtDescr")
    linkedToProductLocator = (By.ID, "")
    subCategoryNameLocator = (By.ID, "")
    subCategoryDescriptionLocator = (By.ID, "")
    linkedtoCategoryLocator = (By.ID, "")
    articleNameLocator = (By.ID, "")
    articleDesciptionLocator = (By.ID, "")
    linkedTosubCategoryLocator = (By.ID, "")

    buttonSaveLocatorforProducts = (By.ID, "btnSave")











