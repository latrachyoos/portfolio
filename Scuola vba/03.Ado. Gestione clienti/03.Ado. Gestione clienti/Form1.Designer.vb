<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.cmbnazioni = New System.Windows.Forms.ComboBox()
        Me.dgv = New System.Windows.Forms.DataGridView()
        Me.IDCliente = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.Clienti = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.MODIFICA = New System.Windows.Forms.Label()
        Me.LBL1 = New System.Windows.Forms.Label()
        Me.txtid = New System.Windows.Forms.TextBox()
        Me.txtnome = New System.Windows.Forms.TextBox()
        Me.btnmodifica = New System.Windows.Forms.Button()
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'cmbnazioni
        '
        Me.cmbnazioni.FormattingEnabled = True
        Me.cmbnazioni.Location = New System.Drawing.Point(4, 12)
        Me.cmbnazioni.Name = "cmbnazioni"
        Me.cmbnazioni.Size = New System.Drawing.Size(169, 21)
        Me.cmbnazioni.TabIndex = 0
        Me.cmbnazioni.Text = "Seleziona una nazione"
        '
        'dgv
        '
        Me.dgv.AllowUserToAddRows = False
        Me.dgv.AllowUserToDeleteRows = False
        Me.dgv.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.dgv.Columns.AddRange(New System.Windows.Forms.DataGridViewColumn() {Me.IDCliente, Me.Clienti})
        Me.dgv.Location = New System.Drawing.Point(179, 12)
        Me.dgv.Name = "dgv"
        Me.dgv.ReadOnly = True
        Me.dgv.Size = New System.Drawing.Size(254, 312)
        Me.dgv.TabIndex = 1
        '
        'IDCliente
        '
        Me.IDCliente.HeaderText = "ID Cliente"
        Me.IDCliente.Name = "IDCliente"
        Me.IDCliente.ReadOnly = True
        '
        'Clienti
        '
        Me.Clienti.HeaderText = "Clienti"
        Me.Clienti.Name = "Clienti"
        Me.Clienti.ReadOnly = True
        '
        'MODIFICA
        '
        Me.MODIFICA.AutoSize = True
        Me.MODIFICA.Font = New System.Drawing.Font("Microsoft Sans Serif", 14.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.MODIFICA.Location = New System.Drawing.Point(38, 54)
        Me.MODIFICA.Name = "MODIFICA"
        Me.MODIFICA.Size = New System.Drawing.Size(100, 24)
        Me.MODIFICA.TabIndex = 2
        Me.MODIFICA.Text = "MODIFICA"
        '
        'LBL1
        '
        Me.LBL1.AutoSize = True
        Me.LBL1.Font = New System.Drawing.Font("Microsoft Sans Serif", 6.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LBL1.Location = New System.Drawing.Point(10, 78)
        Me.LBL1.Name = "LBL1"
        Me.LBL1.Size = New System.Drawing.Size(156, 12)
        Me.LBL1.TabIndex = 3
        Me.LBL1.Text = "DOPPIO CLICK PER MODIFICARE"
        '
        'txtid
        '
        Me.txtid.Enabled = False
        Me.txtid.Location = New System.Drawing.Point(12, 102)
        Me.txtid.Name = "txtid"
        Me.txtid.Size = New System.Drawing.Size(154, 20)
        Me.txtid.TabIndex = 4
        Me.txtid.Text = "ID"
        '
        'txtnome
        '
        Me.txtnome.Enabled = False
        Me.txtnome.Location = New System.Drawing.Point(12, 128)
        Me.txtnome.Name = "txtnome"
        Me.txtnome.Size = New System.Drawing.Size(154, 20)
        Me.txtnome.TabIndex = 5
        Me.txtnome.Text = "CLIENTE"
        '
        'btnmodifica
        '
        Me.btnmodifica.BackColor = System.Drawing.Color.Transparent
        Me.btnmodifica.Enabled = False
        Me.btnmodifica.Location = New System.Drawing.Point(12, 154)
        Me.btnmodifica.Name = "btnmodifica"
        Me.btnmodifica.Size = New System.Drawing.Size(154, 31)
        Me.btnmodifica.TabIndex = 6
        Me.btnmodifica.Text = "MODIFICA"
        Me.btnmodifica.UseVisualStyleBackColor = False
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(451, 339)
        Me.Controls.Add(Me.btnmodifica)
        Me.Controls.Add(Me.txtnome)
        Me.Controls.Add(Me.txtid)
        Me.Controls.Add(Me.LBL1)
        Me.Controls.Add(Me.MODIFICA)
        Me.Controls.Add(Me.dgv)
        Me.Controls.Add(Me.cmbnazioni)
        Me.Name = "Form1"
        Me.Text = "Form1"
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents cmbnazioni As System.Windows.Forms.ComboBox
    Friend WithEvents dgv As System.Windows.Forms.DataGridView
    Friend WithEvents IDCliente As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents Clienti As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents MODIFICA As System.Windows.Forms.Label
    Friend WithEvents LBL1 As System.Windows.Forms.Label
    Friend WithEvents txtid As System.Windows.Forms.TextBox
    Friend WithEvents txtnome As System.Windows.Forms.TextBox
    Friend WithEvents btnmodifica As System.Windows.Forms.Button

End Class
